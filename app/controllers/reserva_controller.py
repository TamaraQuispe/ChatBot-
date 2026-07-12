"""Adapter: ReservaController legacy → nueva arquitectura."""

from app.services.reserva_service import ReservaService
from app.logger import get_logger
from app.utils import escapar

logger = get_logger("reserva")


class ReservaController:
    def __init__(self, db=None):
        self.reserva_service = ReservaService()

    def buscar_disponibilidad(self, palabra_clave: str) -> list:
        try:
            return self.reserva_service.buscar_disponibilidad(palabra_clave)
        except Exception as e:
            logger.error(f"Error buscando disponibilidad: {e}")
            return []

    def procesar_reserva(self, id_usuario: int, id_espacio: int,
                         fecha: str = "2026-05-28") -> bool:
        try:
            if not isinstance(id_usuario, int) or id_usuario <= 0:
                return False
            if not isinstance(id_espacio, int) or id_espacio <= 0:
                return False
            resultado = self.reserva_service.crear(id_usuario, id_espacio, fecha)
            return resultado is not None
        except Exception as e:
            logger.error(f"Error al procesar reserva: {e}")
            return False
