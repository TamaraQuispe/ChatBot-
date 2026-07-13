"""Repositorio de sesiones de chat y mensajes."""

from typing import Optional
from app.repositories.base import BaseRepository
from app.database.connection import fetch_one, fetch_all


class SesionChatRepository(BaseRepository):
    table = "sesiones_chat"
    pk = "id_sesion"

    def get_by_usuario(self, id_usuario: int) -> list:
        return fetch_all(
            "SELECT * FROM sesiones_chat WHERE id_usuario = %s "
            "ORDER BY updated_at DESC",
            (id_usuario,),
        )

    def create(self, id_usuario: int, titulo: str = "Nuevo Chat") -> Optional[dict]:
        return fetch_one(
            "INSERT INTO sesiones_chat (id_usuario, titulo) "
            "VALUES (%s, %s) RETURNING *",
            (id_usuario, titulo),
        )

    def delete(self, id_sesion: int, id_usuario: int) -> bool:
        from app.database.connection import execute
        execute(
            "DELETE FROM mensajes_chat WHERE id_sesion = %s",
            (id_sesion,),
        )
        affected = execute(
            "DELETE FROM sesiones_chat WHERE id_sesion = %s AND id_usuario = %s",
            (id_sesion, id_usuario),
        )
        return affected > 0

    def pertenece_a_usuario(self, id_sesion: int, id_usuario: int) -> bool:
        row = fetch_one(
            "SELECT 1 FROM sesiones_chat WHERE id_sesion = %s AND id_usuario = %s",
            (id_sesion, id_usuario),
        )
        return row is not None

    def actualizar_actividad(self, id_sesion: int) -> bool:
        from app.database.connection import execute
        affected = execute(
            "UPDATE sesiones_chat SET updated_at = NOW() WHERE id_sesion = %s",
            (id_sesion,),
        )
        return affected > 0

    def update_titulo(self, id_sesion: int, titulo: str) -> bool:
        from app.database.connection import execute
        affected = execute(
            "UPDATE sesiones_chat SET titulo = %s, updated_at = NOW() "
            "WHERE id_sesion = %s",
            (titulo, id_sesion),
        )
        return affected > 0


class MensajeChatRepository(BaseRepository):
    table = "mensajes_chat"
    pk = "id_mensaje"

    def get_by_sesion(self, id_sesion: int) -> list:
        return fetch_all(
            "SELECT * FROM mensajes_chat WHERE id_sesion = %s "
            "ORDER BY created_at ASC",
            (id_sesion,),
        )

    def create(self, id_sesion: int, tipo: str, contenido: str) -> Optional[dict]:
        return fetch_one(
            "INSERT INTO mensajes_chat (id_sesion, tipo, contenido) "
            "VALUES (%s, %s, %s) RETURNING *",
            (id_sesion, tipo, contenido),
        )
