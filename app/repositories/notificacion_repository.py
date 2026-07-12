"""Repositorio de notificaciones."""

from app.repositories.base import BaseRepository
from app.database.connection import fetch_one, fetch_all


class NotificacionRepository(BaseRepository):
    table = "notificaciones"
    pk = "id_notificacion"

    def get_by_usuario(self, id_usuario: int, limit: int = 20) -> list:
        return fetch_all(
            "SELECT * FROM notificaciones WHERE id_usuario = %s "
            "ORDER BY created_at DESC LIMIT %s",
            (id_usuario, limit),
        )

    def count_no_leidas(self, id_usuario: int) -> int:
        row = fetch_one(
            "SELECT COUNT(*) as count FROM notificaciones "
            "WHERE id_usuario = %s AND leida = false",
            (id_usuario,),
        )
        return row["count"] if row else 0

    def create(self, id_usuario: int, titulo: str, mensaje: str,
               tipo: str = "info") -> dict:
        return fetch_one(
            "INSERT INTO notificaciones (id_usuario, titulo, mensaje, tipo) "
            "VALUES (%s, %s, %s, %s) RETURNING *",
            (id_usuario, titulo, mensaje, tipo),
        )

    def marcar_leida(self, id_notificacion: int) -> bool:
        from app.database.connection import execute
        affected = execute(
            "UPDATE notificaciones SET leida = true WHERE id_notificacion = %s",
            (id_notificacion,),
        )
        return affected > 0

    def marcar_todas_leidas(self, id_usuario: int) -> bool:
        from app.database.connection import execute
        execute(
            "UPDATE notificaciones SET leida = true "
            "WHERE id_usuario = %s AND leida = false",
            (id_usuario,),
        )
        return True
