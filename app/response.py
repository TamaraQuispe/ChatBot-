"""Formato de respuesta estándar para todas las API."""

import json
from typing import Any
from http.server import BaseHTTPRequestHandler
from app.logger import get_logger

logger = get_logger("response")


def success_response(
    data: Any = None,
    message: str = "Operación exitosa",
    status_code: int = 200,
) -> tuple[str, int, dict]:
    body = json.dumps(
        {"success": True, "message": message, "data": data},
        ensure_ascii=False,
        default=str,
    )
    headers = {"Content-Type": "application/json; charset=utf-8"}
    return body, status_code, headers


def error_response(
    message: str = "Error interno",
    status_code: int = 400,
    errors: list | None = None,
    data: Any = None,
) -> tuple[str, int, dict]:
    body = json.dumps(
        {
            "success": False,
            "message": message,
            "data": data,
            "errors": errors or [],
        },
        ensure_ascii=False,
        default=str,
    )
    headers = {"Content-Type": "application/json; charset=utf-8"}
    return body, status_code, headers


def html_response(
    html_content: str,
    status_code: int = 200,
    extra_headers: dict | None = None,
) -> tuple[str, int, dict]:
    headers = {"Content-Type": "text/html; charset=utf-8"}
    if extra_headers:
        headers.update(extra_headers)
    return html_content, status_code, headers


def redirect_response(location: str) -> tuple[str, int, dict]:
    headers = {"Location": location}
    return "", 302, headers


def send_response(handler: BaseHTTPRequestHandler, body: str, status: int, headers: dict):
    try:
        handler.send_response(status)
        for key, value in headers.items():
            handler.send_header(key, value)
        handler.send_header("Content-Length", str(len(body.encode("utf-8"))))
        handler.end_headers()
        handler.wfile.write(body.encode("utf-8"))
    except Exception as e:
        logger.warning(f"Error al enviar respuesta: {e}")


def send_json(handler: BaseHTTPRequestHandler, data: Any, status: int = 200):
    body, status_code, headers = success_response(data, status_code=status)
    send_response(handler, body, status_code, headers)


def send_error_json(
    handler: BaseHTTPRequestHandler,
    message: str,
    status: int = 400,
    errors: list | None = None,
):
    body, status_code, headers = error_response(message, status, errors)
    send_response(handler, body, status_code, headers)
