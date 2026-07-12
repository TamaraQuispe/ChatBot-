"""Repositorio de reservas."""

from typing import Optional
from app.repositories.base import BaseRepository
from app.database.connection import fetch_one, fetch_all


class ReservaRepository(BaseRepository):
    table = "reservas"
    pk = "id_reserva"

    def get_by_id_with_details(self, id_reserva: int) -> Optional[dict]:
        return fetch_one(
            "SELECT r.*, e.nombre AS espacio_nombre, u.nombre AS usuario_nombre, "
            "u.username FROM reservas r "
            "JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
            "JOIN usuarios u ON r.id_usuario = u.id_usuario "
            "WHERE r.id_reserva = %s",
            (id_reserva,),
        )

    def get_by_usuario(self, id_usuario: int) -> list:
        return fetch_all(
            "SELECT r.*, e.nombre AS espacio_nombre, t.nombre AS tipo_nombre "
            "FROM reservas r "
            "JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
            "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
            "WHERE r.id_usuario = %s ORDER BY r.fecha_creacion DESC",
            (id_usuario,),
        )

    def get_activas(self) -> list:
        return fetch_all(
            "SELECT r.*, e.nombre AS espacio_nombre, u.nombre AS usuario_nombre, "
            "u.username FROM reservas r "
            "JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
            "JOIN usuarios u ON r.id_usuario = u.id_usuario "
            "WHERE r.estado = 'CONFIRMADA' OR r.estado = '1' "
            "ORDER BY r.fecha DESC"
        )

    def get_pendientes(self) -> list:
        return fetch_all(
            "SELECT r.*, e.nombre AS espacio_nombre, u.nombre AS usuario_nombre, "
            "u.username FROM reservas r "
            "JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
            "JOIN usuarios u ON r.id_usuario = u.id_usuario "
            "WHERE r.estado = 'PENDIENTE' ORDER BY r.fecha_creacion DESC"
        )

    def create(self, data: dict) -> Optional[dict]:
        return fetch_one(
            "INSERT INTO reservas (id_usuario, id_espacio, curso_nombre, "
            "horario, fecha, estado) "
            "VALUES (%s, %s, %s, %s, %s, 'CONFIRMADA') RETURNING *",
            (data["id_usuario"], data["id_espacio"], data["curso_nombre"],
             data["horario"], data["fecha"]),
        )

    def cancelar(self, id_reserva: int) -> bool:
        from app.database.connection import execute
        affected = execute(
            "UPDATE reservas SET estado = 'CANCELADA' WHERE id_reserva = %s",
            (id_reserva,),
        )
        return affected > 0

    def update_estado(self, id_reserva: int, estado: str) -> bool:
        from app.database.connection import execute
        affected = execute(
            "UPDATE reservas SET estado = %s WHERE id_reserva = %s",
            (estado, id_reserva),
        )
        return affected > 0

    def get_by_espacio(self, id_espacio: int) -> list:
        return fetch_all(
            "SELECT r.*, u.nombre AS usuario_nombre, u.username "
            "FROM reservas r JOIN usuarios u ON r.id_usuario = u.id_usuario "
            "WHERE r.id_espacio = %s ORDER BY r.fecha DESC",
            (id_espacio,),
        )
