import sys, os, io

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import UTPHandler as _BaseHandler


class _VercelHandler(_BaseHandler):
    rbufsize = 0
    wbufsize = 0

    def handle(self):
        self.handle_one_request()

    def finish(self):
        pass


def app(environ, start_response):
    method = environ["REQUEST_METHOD"]
    path = environ.get("PATH_INFO", "/")
    qs = environ.get("QUERY_STRING", "")
    if qs:
        path += "?" + qs

    content_length = int(environ.get("CONTENT_LENGTH", 0) or 0)
    body = environ["wsgi.input"].read(content_length) if content_length else b""

    req = f"{method} {path} HTTP/1.1\r\n"
    req += f"Host: {environ.get('HTTP_HOST', environ.get('SERVER_NAME', 'localhost'))}\r\n"
    req += "Connection: close\r\n"

    for key, value in environ.items():
        if key == "HTTP_COOKIE":
            req += f"Cookie: {value}\r\n"
        elif key.startswith("HTTP_"):
            header_name = key[5:].replace("_", "-").title()
            req += f"{header_name}: {value}\r\n"

    if "CONTENT_TYPE" in environ:
        req += f"Content-Type: {environ['CONTENT_TYPE']}\r\n"
    if content_length:
        req += f"Content-Length: {content_length}\r\n"
    req += "\r\n"

    raw_request = req.encode("utf-8") + body

    response_buf = io.BytesIO()

    class _FakeSocket:
        def makefile(self, mode, bufsize=None):
            if "r" in mode:
                return io.BufferedReader(io.BytesIO(raw_request))
            return io.BufferedWriter(io.BytesIO())

        def sendall(self, data):
            response_buf.write(data)

        def getsockname(self):
            return ("0.0.0.0", 0)

        def fileno(self):
            raise io.UnsupportedOperation("fileno")

    class _FakeServer:
        def __init__(self):
            self.server_name = environ.get("SERVER_NAME", "localhost")
            self.server_port = int(environ.get("SERVER_PORT", "80"))
            self.socket = _FakeSocket()

    _VercelHandler(_FakeSocket(), ("127.0.0.1", 0), _FakeServer())

    raw_resp = response_buf.getvalue().decode("utf-8", errors="replace")

    header_end = raw_resp.find("\r\n\r\n")
    if header_end == -1:
        start_response("500 Internal Server Error", [("Content-Type", "text/plain")])
        return [b"Handler produced no parsable response"]

    header_section = raw_resp[:header_end]
    body_text = raw_resp[header_end + 4:]

    lines = header_section.split("\r\n")
    status_line = lines[0]
    status_code = status_line.split(" ", 1)[1] if " " in status_line else "200 OK"

    wsgi_headers = []
    for line in lines[1:]:
        if ":" in line:
            key, value = line.split(":", 1)
            wsgi_headers.append((key.strip(), value.strip()))

    start_response(status_code, wsgi_headers)
    return [body_text.encode("utf-8")]
