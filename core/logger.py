import os
import logging
from datetime import datetime

LOG_DIR = os.environ.get("LOG_DIR", "logs")
try:
    os.makedirs(LOG_DIR, exist_ok=True)
    test_file = os.path.join(LOG_DIR, ".vercel_write_test")
    with open(test_file, "w") as f:
        f.write("ok")
    os.remove(test_file)
    _writable = True
except (OSError, PermissionError):
    LOG_DIR = "/tmp/logs"
    os.makedirs(LOG_DIR, exist_ok=True)
    _writable = True


def get_logger(nombre="app"):
    logger = logging.getLogger(nombre)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        try:
            archivo = logging.FileHandler(
                os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log"),
                encoding="utf-8"
            )
            archivo.setFormatter(formatter)
            logger.addHandler(archivo)
        except (OSError, PermissionError):
            pass
        consola = logging.StreamHandler()
        consola.setFormatter(formatter)
        logger.addHandler(consola)
    return logger
