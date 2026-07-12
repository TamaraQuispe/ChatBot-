"""Repositorio de docentes."""

from typing import Optional
from app.repositories.base import BaseRepository
from app.database.connection import fetch_one, fetch_all


class DocenteRepository(BaseRepository):
    table = "docentes"
    pk = "id_docente"

    def get_all_with_details(self) -> list:
        return fetch_all(
            "SELECT d.*, u.nombre AS usuario_nombre, u.username "
            "FROM docentes d "
            "LEFT JOIN usuarios u ON d.id_usuario = u.id_usuario "
            "ORDER BY d.nombre"
        )
