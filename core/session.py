"""Adapter: Sesiones legacy → nueva arquitectura JWT."""

from app.auth.jwt import (
    verify_token as _verify,
    create_access_token as _create,
    get_session_from_cookie as _from_cookie,
    make_set_cookie_header as _make_set,
    make_clear_cookie_header as _make_clear,
)

_COOKIE_NAME = "utp_session"


def _sign(data: str) -> str:
    import hashlib, hmac, os
    secret = os.environ.get("SESSION_SECRET", "utp-chatbot-secret-dev-key-2024")
    return hmac.new(secret.encode(), data.encode(), hashlib.sha256).hexdigest()[:16]


def _encode(payload: dict) -> str:
    import json, base64
    raw = json.dumps(payload, separators=(",", ":"), ensure_ascii=False, default=str)
    return base64.urlsafe_b64encode(raw.encode()).decode().rstrip("=")


def _decode(data: str):
    import json, base64
    try:
        padded = data + "=" * (4 - len(data) % 4) if len(data) % 4 else data
        raw = base64.urlsafe_b64decode(padded.encode()).decode()
        return json.loads(raw)
    except Exception:
        return None


def _make_token(payload: dict) -> str:
    b64 = _encode(payload)
    sig = _sign(b64)
    return f"{sig}.{b64}"


def _parse_token(token: str):
    import hmac
    try:
        sig, b64 = token.split(".", 1)
        expected = _sign(b64)
        if not hmac.compare_digest(sig, expected):
            return None
        return _decode(b64)
    except (ValueError, json.JSONDecodeError):
        return None


def create_session(usuario: dict) -> str:
    payload = {
        "id_usuario": usuario["id_usuario"],
        "username": usuario["username"],
        "rol": usuario["rol"],
        "nombre": usuario["nombre"],
        "correo": usuario.get("correo", ""),
    }
    return _make_token(payload)


def get_session(cookie_header):
    return _from_cookie(cookie_header)


def make_set_cookie_header(usuario: dict) -> str:
    from app.auth.jwt import make_set_cookie_header as msc
    return msc(usuario)


def make_clear_cookie_header(cookie_name=None):
    name = cookie_name or _COOKIE_NAME
    return f"{name}=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0"
