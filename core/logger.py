import os
import logging
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(nombre="app"):
    logger = logging.getLogger(nombre)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        archivo = logging.FileHandler(
            os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log"),
            encoding="utf-8"
        )
        archivo.setFormatter(formatter)
        logger.addHandler(archivo)
        consola = logging.StreamHandler()
        consola.setFormatter(formatter)
        logger.addHandler(consola)
    return logger
