"""Adapter: GestorReservas legacy → nueva arquitectura."""

from typing import Optional
from app.services.reserva_service import ReservaService
from app.logger import get_logger

logger = get_logger("gestor_reservas")


class GestorReservas:
    def __init__(self, db=None):
        self.service = ReservaService()

    def crear_reserva(self, id_usuario: int, id_espacio: int,
                      fecha: str = "2026-05-28") -> bool:
        try:
            result = self.service.crear(id_usuario, id_espacio, fecha)
            return result is not None
        except Exception as e:
            logger.error(f"Error al crear reserva: {e}")
            return False

    def cancelar_reserva(self, id_reserva: int) -> bool:
        try:
            return self.service.cancelar(id_reserva)
        except Exception as e:
            logger.error(f"Error al cancelar reserva: {e}")
            return False

    def listar_reservas_activas(self) -> list:
        return self.service.listar_activas()

    def reservas_por_usuario(self, id_usuario: int) -> list:
        return self.service.listar_por_usuario(id_usuario)
