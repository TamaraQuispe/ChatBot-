"""Adapter: Espacio model legacy → nueva arquitectura."""

from typing import Optional
from app.repositories.espacio_repository import EspacioRepository
from app.services.espacio_service import EspacioService
from app.logger import get_logger

logger = get_logger("espacio")


class EspacioAcademico:
    def __init__(self, db=None):
        self.repo = EspacioRepository()
        self.service = EspacioService()

    def buscar_disponibles(self, tipo: str) -> list:
        return self.service.buscar_disponibles(tipo)

    def listar_todos(self) -> list:
        return self.repo.get_all()

    def ocupar(self, id_espacio: int) -> bool:
        return self.service.ocupar(id_espacio)

    def liberar(self, id_espacio: int) -> bool:
        return self.service.liberar(id_espacio)
