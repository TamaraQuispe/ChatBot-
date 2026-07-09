import html
from datetime import datetime, timedelta
from typing import Optional
from config.database import Database
from core.logger import get_logger

logger = get_logger("utils")


def escapar(texto: str) -> str:
    if texto is None:
        return ""
    return html.escape(str(texto), quote=True)


def liberar_espacios_vencidos(db: Database, horas_max: int = 2) -> int:
    conn = None
    try:
        conn = db.obtener_conexion()
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
            conn.commit()
            logger.info(f"Espacios liberados automaticamente: {liberados}")
        conn.close()
        return liberados
    except Exception as e:
        logger.error(f"Error liberando espacios vencidos: {e}")
        return 0
