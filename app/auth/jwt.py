"""Manejo de JWT tokens para autenticación."""

import os
import json
import base64
import hashlib
import hmac
import secrets
import time
from typing import Optional
from http.cookies import SimpleCookie
from app.logger import get_logger

logger = get_logger("auth")

_SECRET = os.environ.get("JWT_SECRET") or os.environ.get(
    "SESSION_SECRET", "utp-chatbot-secret-dev-key-2024"
)
_ACCESS_TOKEN_EXPIRY = int(os.environ.get("JWT_ACCESS_EXPIRY", "86400"))
_REFRESH_TOKEN_EXPIRY = int(os.environ.get("JWT_REFRESH_EXPIRY", "2592000"))
_COOKIE_NAME = os.environ.get("SESSION_COOKIE", "utp_session")


def _base64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def _base64url_decode(data: str) -> bytes:
    padded = data + "=" * (4 - len(data) % 4) if len(data) % 4 else data
    return base64.urlsafe_b64decode(padded.encode())


def _sign(data: str) -> str:
    return hmac.new(_SECRET.encode(), data.encode(), hashlib.sha256).hexdigest()[:16]


def _verify_sign(data: str, sig: str) -> bool:
    expected = _sign(data)
    return hmac.compare_digest(sig, expected)


def create_access_token(payload: dict) -> str:
    token_payload = {
        **payload,
        "type": "access",
        "iat": int(time.time()),
        "exp": int(time.time()) + _ACCESS_TOKEN_EXPIRY,
    }
    raw = json.dumps(token_payload, separators=(",", ":"), ensure_ascii=False)
    b64 = _base64url_encode(raw.encode())
    sig = _sign(b64)
    return f"{sig}.{b64}"


def create_refresh_token(payload: dict) -> str:
    token_payload = {
        **payload,
        "type": "refresh",
        "iat": int(time.time()),
        "exp": int(time.time()) + _REFRESH_TOKEN_EXPIRY,
        "jti": secrets.token_hex(16),
    }
    raw = json.dumps(token_payload, separators=(",", ":"), ensure_ascii=False)
    b64 = _base64url_encode(raw.encode())
    sig = _sign(b64)
    return f"{sig}.{b64}"


def verify_token(token: str) -> Optional[dict]:
    try:
        parts = token.split(".", 1)
        if len(parts) != 2:
            return None
        sig, b64 = parts
        if not _verify_sign(b64, sig):
            return None
        raw = _base64url_decode(b64).decode()
        payload = json.loads(raw)
        if payload.get("exp", 0) < time.time():
            return None
        return payload
    except (ValueError, json.JSONDecodeError, Exception) as e:
        logger.warning(f"Error verificando token: {e}")
        return None


def create_session_token(usuario: dict) -> str:
    payload = {
        "id_usuario": usuario["id_usuario"],
        "username": usuario["username"],
        "rol": usuario["rol"],
        "nombre": usuario["nombre"],
        "correo": usuario.get("correo", ""),
    }
    return create_access_token(payload)


def get_session_from_cookie(cookie_header: Optional[str]) -> Optional[dict]:
    if not cookie_header:
        return None
    try:
        c = SimpleCookie()
        c.load(cookie_header)
        if _COOKIE_NAME not in c:
            return None
        return verify_token(c[_COOKIE_NAME].value)
    except Exception as e:
        logger.warning(f"Error al leer cookie: {e}")
        return None


def get_session_from_headers(headers: dict) -> Optional[dict]:
    auth = headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        return verify_token(auth[7:])
    return get_session_from_cookie(headers.get("Cookie"))


def make_set_cookie_header(usuario: dict) -> str:
    token = create_session_token(usuario)
    max_age = _ACCESS_TOKEN_EXPIRY
    return (
        f"{_COOKIE_NAME}={token}; HttpOnly; SameSite=Lax; "
        f"Path=/; Max-Age={max_age}"
    )


def make_clear_cookie_header(cookie_name: str | None = None) -> str:
    name = cookie_name or _COOKIE_NAME
    return f"{name}=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0"
