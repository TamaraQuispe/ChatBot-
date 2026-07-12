"""Servicio de espacios académicos."""

from typing import Optional
from app.repositories.espacio_repository import EspacioRepository
from app.repositories.reserva_repository import ReservaRepository
from app.logger import get_logger
from app.exceptions import NotFoundError

logger = get_logger("espacio_service")


class EspacioService:
    def __init__(self):
        self.repo = EspacioRepository()
        self.reserva_repo = ReservaRepository()

    def listar_todos(self) -> list:
        return self.repo.get_all_with_details()

    def obtener_por_id(self, id_espacio: int) -> dict:
        espacio = self.repo.get_by_id_with_tipo(id_espacio)
        if not espacio:
            raise NotFoundError("Espacio")
        return espacio

    def obtener_tipos(self) -> list:
        return self.repo.get_tipos()

    def obtener_equipamientos(self) -> list:
        return self.repo.get_equipamientos()

    def obtener_software(self) -> list:
        return self.repo.get_software_all()

    def obtener_equipamientos_por_espacio(self, id_espacio: int) -> set:
        return self.repo.get_equipamientos_by_espacio(id_espacio)

    def obtener_software_por_espacio(self, id_espacio: int) -> set:
        return self.repo.get_software_by_espacio(id_espacio)

    def actualizar(self, id_espacio: int, data: dict) -> bool:
        espacio = self.repo.get_by_id(id_espacio)
        if not espacio:
            raise NotFoundError("Espacio")
        return self.repo.update(id_espacio, data)

    def cambiar_estado(self, id_espacio: int, estado: str) -> bool:
        espacio = self.repo.get_by_id(id_espacio)
        if not espacio:
            raise NotFoundError("Espacio")
        return self.repo.cambiar_estado(id_espacio, estado)

    def eliminar(self, id_espacio: int) -> bool:
        from app.database.connection import get_connection
        espacio = self.repo.get_by_id(id_espacio)
        if not espacio:
            raise NotFoundError("Espacio")
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM reservas WHERE id_espacio = %s", (id_espacio,))
            cur.execute("DELETE FROM espacio_equipamiento WHERE id_espacio = %s", (id_espacio,))
            cur.execute("DELETE FROM espacio_software WHERE id_espacio = %s", (id_espacio,))
            cur.execute("DELETE FROM espacios_academicos WHERE id_espacio = %s", (id_espacio,))
        logger.info(f"Espacio eliminado: id={id_espacio}")
        return True

    def get_all_with_details_and_relations(self) -> list:
        from app.database.connection import fetch_all, fetch_one
        try:
            espacios = self.repo.get_all_with_details()
            result = []
            for e in espacios:
                d = dict(e)
                id_esp = d["id_espacio"]
                d["tipo"] = d.pop("tipo_nombre", d.get("tipo", ""))
                equipos = fetch_all(
                    "SELECT eq.nombre FROM espacio_equipamiento ee "
                    "JOIN equipamientos eq ON ee.id_equipamiento = eq.id_equipamiento "
                    "WHERE ee.id_espacio = %s", (id_esp,)
                )
                softwares = fetch_all(
                    "SELECT s.nombre FROM espacio_software es "
                    "JOIN software s ON es.id_software = s.id_software "
                    "WHERE es.id_espacio = %s", (id_esp,)
                )
                d["equipamiento"] = ", ".join(r["nombre"] for r in equipos) if equipos else ""
                d["software"] = ", ".join(r["nombre"] for r in softwares) if softwares else "Ninguno"
                result.append(d)
            return result
        except Exception as e:
            logger.error(f"Error obteniendo espacios con relaciones: {e}")
            return []

    def get_activos_with_details(self) -> list:
        from app.database.connection import fetch_all
        try:
            espacios = fetch_all(
                "SELECT e.id_espacio, e.nombre, t.nombre AS tipo, e.estado "
                "FROM espacios_academicos e "
                "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
                "ORDER BY e.nombre"
            )
            result = []
            for e in espacios:
                d = dict(e)
                id_esp = d["id_espacio"]
                equipos = fetch_all(
                    "SELECT eq.nombre FROM espacio_equipamiento ee "
                    "JOIN equipamientos eq ON ee.id_equipamiento = eq.id_equipamiento "
                    "WHERE ee.id_espacio = %s", (id_esp,)
                )
                softwares = fetch_all(
                    "SELECT s.nombre, s.version FROM espacio_software es "
                    "JOIN software s ON es.id_software = s.id_software "
                    "WHERE es.id_espacio = %s", (id_esp,)
                )
                d["equipamiento"] = ", ".join(r["nombre"] for r in equipos) if equipos else ""
                d["software"] = ", ".join(
                    f"{r['nombre']} {r['version'] or ''}".strip() for r in softwares
                ) if softwares else ""
                result.append(d)
            return result
        except Exception as e:
            logger.error(f"Error obteniendo activos: {e}")
            return []

    def buscar_disponibles(self, tipo: str) -> list:
        from app.database.connection import fetch_all
        try:
            return fetch_all(
                "SELECT e.*, t.nombre AS tipo FROM espacios_academicos e "
                "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
                "WHERE t.nombre = %s AND e.estado = 'DISPONIBLE'",
                (tipo,)
            )
        except Exception as e:
            logger.error(f"Error buscando disponibles: {e}")
            return []

    def ocupar(self, id_espacio: int) -> bool:
        from app.database.connection import execute
        try:
            execute(
                "UPDATE espacios_academicos SET estado = 'OCUPADO' WHERE id_espacio = %s",
                (id_espacio,)
            )
            return True
        except Exception as e:
            logger.error(f"Error ocupando espacio: {e}")
            return False

    def liberar(self, id_espacio: int) -> bool:
        from app.database.connection import execute
        try:
            execute(
                "UPDATE espacios_academicos SET estado = 'DISPONIBLE' WHERE id_espacio = %s",
                (id_espacio,)
            )
            return True
        except Exception as e:
            logger.error(f"Error liberando espacio: {e}")
            return False
