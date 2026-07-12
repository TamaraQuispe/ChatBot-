"""Rate limiting simple en memoria."""

import time
import os
from collections import defaultdict
from typing import Callable
from app.logger import get_logger

logger = get_logger("middleware")

_RATE_LIMIT = int(os.environ.get("RATE_LIMIT_REQUESTS", "60"))
_RATE_WINDOW = int(os.environ.get("RATE_LIMIT_WINDOW", "60"))

_requests: dict[str, list] = defaultdict(list)


def check_rate_limit(ip: str) -> bool:
    now = time.time()
    window_start = now - _RATE_WINDOW
    _requests[ip] = [t for t in _requests[ip] if t > window_start]
    if len(_requests[ip]) >= _RATE_LIMIT:
        logger.warning(f"Rate limit excedido para {ip}")
        return False
    _requests[ip].append(now)
    return True
