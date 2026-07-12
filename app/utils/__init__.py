"""Utilidades generales del aplicativo."""

import html
import re
from datetime import datetime, timedelta
from app.database.connection import get_connection
from app.logger import get_logger

logger = get_logger("utils")

_USERNAME_PATTERN = re.compile(r"^[a-zA-Z0-9_]{3,50}$")
_EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def escapar(texto: str | None) -> str:
    if texto is None:
        return ""
    return html.escape(str(texto), quote=True)


def sanitizar(texto: str) -> str:
    return html.escape(str(texto).strip(), quote=True)


def validar_username(username: str) -> bool:
    return bool(_USERNAME_PATTERN.match(username))


def validar_email(email: str) -> bool:
    return bool(_EMAIL_PATTERN.match(email))


def validar_password(password: str) -> tuple[bool, str]:
    if len(password) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres"
    if len(password) > 128:
        return False, "La contraseña no puede exceder 128 caracteres"
    return True, ""


def parse_int(valor: str | int | None, default: int = 0) -> int:
    if valor is None:
        return default
    try:
        return int(valor)
    except (ValueError, TypeError):
        return default


def liberar_espacios_vencidos(horas_max: int = 2) -> int:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            limite = (datetime.now() - timedelta(hours=horas_max)).isoformat()
            cursor.execute(
                "UPDATE espacios_academicos SET estado = '1' "
                "WHERE CAST(estado AS TEXT) = '2' AND id_espacio IN ("
                "  SELECT r.id_espacio FROM reservas r "
                "  WHERE CAST(r.estado AS TEXT) = '1' AND r.fecha_creacion < %s"
                ")",
                (limite,)
            )
            liberados = cursor.rowcount
            if liberados > 0:
                cursor.execute(
                    "UPDATE reservas SET estado = '2' "
                    "WHERE CAST(estado AS TEXT) = '1' AND fecha_creacion < %s",
                    (limite,)
                )
            if liberados > 0:
                logger.info(f"Espacios liberados automáticamente: {liberados}")
            return liberados
    except Exception as e:
        logger.error(f"Error liberando espacios vencidos: {e}")
        return 0
