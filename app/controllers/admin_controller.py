"""Adapter: AdminController legacy → nueva arquitectura."""

from typing import Optional
from config.database import Database
from app.services.admin_service import AdminService
from app.services.espacio_service import EspacioService
from app.services.reserva_service import ReservaService
from app.logger import get_logger

logger = get_logger("admin")


class AdminController:
    def __init__(self, db: Database = None):
        self.admin_service = AdminService()
        self.espacio_service = EspacioService()
        self.reserva_service = ReservaService()

    def obtener_docentes(self) -> list:
        from app.repositories.docente_repository import DocenteRepository
        try:
            return DocenteRepository().get_all_with_details()
        except Exception as e:
            logger.error(f"Error obteniendo docentes: {e}")
            return []

    def obtener_espacios(self) -> list:
        return self.espacio_service.get_all_with_details_and_relations()

    def obtener_reservas(self) -> list:
        from app.repositories.reserva_repository import ReservaRepository
        try:
            return ReservaRepository().get_activas()
        except Exception as e:
            logger.error(f"Error obteniendo reservas: {e}")
            return []

    def aprobar_reserva(self, id_reserva: int) -> bool:
        try:
            return self.reserva_service.aprobar(id_reserva)
        except Exception as e:
            logger.error(f"Error aprobando reserva: {e}")
            return False

    def rechazar_reserva(self, id_reserva: int) -> bool:
        try:
            return self.reserva_service.rechazar(id_reserva)
        except Exception as e:
            logger.error(f"Error rechazando reserva: {e}")
            return False

    def obtener_estadisticas(self) -> dict:
        return self.admin_service.obtener_estadisticas()

    def obtener_activos(self) -> list:
        return self.espacio_service.get_activos_with_details()

    def eliminar_espacio(self, id_espacio: int) -> bool:
        try:
            return self.espacio_service.eliminar(id_espacio)
        except Exception as e:
            logger.error(f"Error eliminando espacio: {e}")
            return False

    def cambiar_estado_espacio(self, id_espacio: int, estado: str) -> bool:
        try:
            return self.espacio_service.cambiar_estado(id_espacio, estado)
        except Exception as e:
            logger.error(f"Error cambiando estado espacio: {e}")
            return False

    def obtener_usuarios(self) -> list:
        return self.admin_service.obtener_usuarios()

    def obtener_bloques_horario(self) -> list:
        return self.admin_service.obtener_bloques_horario()

    def obtener_facultades(self) -> list:
        return self.admin_service.obtener_facultades()
