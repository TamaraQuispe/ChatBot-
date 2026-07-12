"""Adapter: Reserva model legacy → nueva arquitectura."""

from typing import Optional
from app.repositories.reserva_repository import ReservaRepository
from app.logger import get_logger

logger = get_logger("reserva")


class Reserva:
    def __init__(self, db=None):
        self.repo = ReservaRepository()

    def crear(self, id_usuario: int, id_espacio: int,
              fecha: str = "2026-05-28") -> bool:
        try:
            from app.services.reserva_service import ReservaService
            svc = ReservaService()
            result = svc.crear(id_usuario, id_espacio, fecha)
            return result is not None
        except Exception as e:
            logger.error(f"Error creando reserva: {e}")
            return False

    def listar_por_usuario(self, id_usuario: int) -> list:
        try:
            return self.repo.get_by_usuario(id_usuario)
        except Exception as e:
            logger.error(f"Error listando reservas: {e}")
            return []
