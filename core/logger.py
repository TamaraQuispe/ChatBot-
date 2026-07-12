"""Adapter: Logger legacy → nueva arquitectura."""

from app.logger import get_logger as _new_get_logger

LOG_DIR = __import__("app.logger", fromlist=["LOG_DIR"]).LOG_DIR


def get_logger(nombre="app"):
    return _new_get_logger(nombre)
