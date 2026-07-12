"""Logging profesional con rotación de archivos y formato estructurado."""

import os
import logging
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Optional

_LOG_DIR = os.environ.get("LOG_DIR", "logs")
_LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG").upper()
_MAX_BYTES = 5 * 1024 * 1024
_BACKUP_COUNT = 5


def _ensure_log_dir() -> str:
    try:
        os.makedirs(_LOG_DIR, exist_ok=True)
        test_file = os.path.join(_LOG_DIR, ".write_test")
        with open(test_file, "w") as f:
            f.write("ok")
        os.remove(test_file)
        return _LOG_DIR
    except (OSError, PermissionError):
        fallback = "/tmp/logs"
        os.makedirs(fallback, exist_ok=True)
        return fallback


LOG_DIR = _ensure_log_dir()


def get_logger(nombre: str = "app") -> logging.Logger:
    logger = logging.getLogger(nombre)
    if logger.handlers:
        return logger

    level = getattr(logging, _LOG_LEVEL, logging.DEBUG)
    logger.setLevel(level)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    try:
        file_handler = RotatingFileHandler(
            os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log"),
            maxBytes=_MAX_BYTES,
            backupCount=_BACKUP_COUNT,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except (OSError, PermissionError):
        pass

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
