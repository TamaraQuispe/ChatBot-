"""Repositorio de roles."""

from typing import Optional
from app.repositories.base import BaseRepository
from app.database.connection import fetch_one, fetch_all


class RolRepository(BaseRepository):
    table = "roles"
    pk = "id_rol"

    def get_all_with_permisos(self) -> list:
        return fetch_all(
            "SELECT r.*, COALESCE(p.permisos, '{}') as permisos "
            "FROM roles r "
            "LEFT JOIN rol_permisos p ON r.id_rol = p.id_rol "
            "ORDER BY r.nombre"
        )
