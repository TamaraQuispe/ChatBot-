import os
import json
import hashlib
import hmac
import secrets
import base64
from typing import Optional
from http.cookies import SimpleCookie
from core.logger import get_logger

logger = get_logger("session")

_SECRET = os.environ.get("SESSION_SECRET", "utp-chatbot-secret-dev-key-2024")
_COOKIE_NAME = "utp_session"


def _sign(data: str) -> str:
    return hmac.new(_SECRET.encode(), data.encode(), hashlib.sha256).hexdigest()[:16]


def _encode(payload: dict) -> str:
    raw = json.dumps(payload, separators=(",", ":"), ensure_ascii=False, default=str)
    return base64.urlsafe_b64encode(raw.encode()).decode().rstrip("=")


def _decode(data: str) -> Optional[dict]:
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


def _parse_token(token: str) -> Optional[dict]:
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


def get_session(cookie_header: Optional[str]) -> Optional[dict]:
    if not cookie_header:
        return None
    try:
        c = SimpleCookie()
        c.load(cookie_header)
        if _COOKIE_NAME not in c:
            return None
        return _parse_token(c[_COOKIE_NAME].value)
    except Exception as e:
        logger.warning(f"Error al parsear cookie: {e}")
        return None


def make_set_cookie_header(usuario: dict) -> str:
    token = create_session(usuario)
    return (
        f"{_COOKIE_NAME}={token}; HttpOnly; SameSite=Lax; Path=/; Max-Age=86400"
    )


def make_clear_cookie_header() -> str:
    return f"{_COOKIE_NAME}=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0"
