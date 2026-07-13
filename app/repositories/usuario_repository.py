"""Repositorio de usuarios."""

from typing import Optional
from app.repositories.base import BaseRepository
from app.database.connection import fetch_one, fetch_all


class UsuarioRepository(BaseRepository):
    table = "usuarios"
    pk = "id_usuario"

    def get_by_username(self, username: str) -> Optional[dict]:
        return fetch_one(
            "SELECT u.*, COALESCE(r.nombre, 'Docente') AS rol "
            "FROM usuarios u "
            "LEFT JOIN roles r ON u.id_rol = r.id_rol "
            "WHERE u.username = %s",
            (username,)
        )

    def get_by_correo(self, correo: str) -> Optional[dict]:
        return fetch_one(
            "SELECT * FROM usuarios WHERE correo = %s", (correo,)
        )

    def create(self, data: dict) -> Optional[dict]:
        return fetch_one(
            "INSERT INTO usuarios (username, password, nombre, correo, rol) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING id_usuario, username, nombre, correo, rol",
            (data["username"], data["password"], data["nombre"],
             data["correo"], data.get("rol", "DOCENTE")),
        )

    def update_password(self, id_usuario: int, new_password: str) -> bool:
        affected = self._execute(
            "UPDATE usuarios SET password = %s WHERE id_usuario = %s",
            (new_password, id_usuario),
        )
        return affected > 0

    def get_all_docentes(self) -> list:
        return fetch_all(
            "SELECT id_usuario, username, nombre, correo FROM usuarios WHERE rol = 'DOCENTE' ORDER BY nombre"
        )

    @staticmethod
    def _execute(query: str, params: tuple = ()) -> int:
        from app.database.connection import execute
        return execute(query, params)
