"""Repositorio de espacios académicos."""

from typing import Optional
from app.repositories.base import BaseRepository
from app.database.connection import fetch_one, fetch_all


class EspacioRepository(BaseRepository):
    table = "espacios_academicos"
    pk = "id_espacio"

    def get_by_id_with_tipo(self, id_espacio: int) -> Optional[dict]:
        return fetch_one(
            "SELECT e.*, t.nombre AS tipo_nombre "
            "FROM espacios_academicos e "
            "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
            "WHERE e.id_espacio = %s",
            (id_espacio,),
        )

    def get_all_with_details(self) -> list:
        return fetch_all(
            "SELECT e.*, t.nombre AS tipo "
            "FROM espacios_academicos e "
            "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
            "ORDER BY e.nombre"
        )

    def get_tipos(self) -> list:
        return fetch_all(
            "SELECT id_tipo, nombre FROM tipos_espacio ORDER BY nombre"
        )

    def get_equipamientos(self) -> list:
        return fetch_all(
            "SELECT id_equipamiento, nombre FROM equipamientos ORDER BY nombre"
        )

    def get_software_all(self) -> list:
        return fetch_all(
            "SELECT id_software, nombre FROM software ORDER BY nombre"
        )

    def get_equipamientos_by_espacio(self, id_espacio: int) -> set:
        rows = fetch_all(
            "SELECT id_equipamiento FROM espacio_equipamiento WHERE id_espacio = %s",
            (id_espacio,),
        )
        return {r["id_equipamiento"] for r in rows}

    def get_software_by_espacio(self, id_espacio: int) -> set:
        rows = fetch_all(
            "SELECT id_software FROM espacio_software WHERE id_espacio = %s",
            (id_espacio,),
        )
        return {r["id_software"] for r in rows}

    def update(self, id_espacio: int, data: dict) -> bool:
        from app.database.connection import get_connection
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "UPDATE espacios_academicos SET nombre=%s, id_tipo=%s, "
                "estado=%s, ubicacion=%s, capacidad=%s WHERE id_espacio=%s",
                (data["nombre"], data["id_tipo"], data["estado"],
                 data["ubicacion"], data["capacidad"], id_espacio),
            )
            cur.execute(
                "DELETE FROM espacio_equipamiento WHERE id_espacio = %s",
                (id_espacio,),
            )
            for eq_id in data.get("equipamiento", []):
                cur.execute(
                    "INSERT INTO espacio_equipamiento (id_espacio, id_equipamiento) VALUES (%s, %s)",
                    (id_espacio, int(eq_id)),
                )
            cur.execute(
                "DELETE FROM espacio_software WHERE id_espacio = %s",
                (id_espacio,),
            )
            for sw_id in data.get("software", []):
                cur.execute(
                    "INSERT INTO espacio_software (id_espacio, id_software) VALUES (%s, %s)",
                    (id_espacio, int(sw_id)),
                )
        return True

    def cambiar_estado(self, id_espacio: int, estado: str) -> bool:
        from app.database.connection import execute
        affected = execute(
            "UPDATE espacios_academicos SET estado = %s WHERE id_espacio = %s",
            (estado, id_espacio),
        )
        return affected > 0

    def get_estado_map(self) -> dict:
        return {
            "DISPONIBLE": ("text-emerald-600", "bg-emerald-500", "Disponible"),
            "OCUPADO": ("text-red-600", "bg-red-500", "Ocupado"),
            "MANTENIMIENTO": ("text-amber-600", "bg-amber-500", "Mantenimiento"),
        }
