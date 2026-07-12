"""Middleware CORS para permitir orígenes cruzados."""

import os
from typing import Optional

_ALLOWED_ORIGINS = os.environ.get(
    "CORS_ORIGINS",
    "http://localhost:8000,https://chatbot-inky-kappa.vercel.app",
).split(",")

_ALLOWED_METHODS = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
_ALLOWED_HEADERS = "Content-Type, Authorization, X-Requested-With"


def get_cors_headers(origin: Optional[str] = None) -> dict:
    headers = {}
    if origin and origin in _ALLOWED_ORIGINS:
        headers["Access-Control-Allow-Origin"] = origin
    elif "*" in _ALLOWED_ORIGINS:
        headers["Access-Control-Allow-Origin"] = "*"
    else:
        headers["Access-Control-Allow-Origin"] = (
            _ALLOWED_ORIGINS[0] if _ALLOWED_ORIGINS else "*"
        )
    headers["Access-Control-Allow-Methods"] = _ALLOWED_METHODS
    headers["Access-Control-Allow-Headers"] = _ALLOWED_HEADERS
    headers["Access-Control-Allow-Credentials"] = "true"
    return headers
