"""Adapter: Notificacion model legacy → nueva arquitectura."""

from typing import Optional
from app.repositories.notificacion_repository import NotificacionRepository
from app.logger import get_logger

logger = get_logger("notificacion")


class Notificacion:
    def __init__(self, db=None):
        self.repo = NotificacionRepository()

    def listar(self, id_usuario: int) -> list:
        return self.repo.get_by_usuario(id_usuario)

    def contar_no_leidas(self, id_usuario: int) -> int:
        return self.repo.count_no_leidas(id_usuario)

    def crear(self, id_usuario: int, titulo: str, mensaje: str,
              tipo: str = "info") -> dict:
        return self.repo.create(id_usuario, titulo, mensaje, tipo)

    def marcar_leida(self, id_notificacion: int) -> bool:
        return self.repo.marcar_leida(id_notificacion)

    def marcar_todas_leidas(self, id_usuario: int) -> bool:
        return self.repo.marcar_todas_leidas(id_usuario)

    @staticmethod
    def crear_tabla(db=None):
        pass
