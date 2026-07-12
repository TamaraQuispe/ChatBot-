"""Servicio de reservas."""

from typing import Optional
from app.repositories.reserva_repository import ReservaRepository
from app.repositories.espacio_repository import EspacioRepository
from app.repositories.notificacion_repository import NotificacionRepository
from app.logger import get_logger
from app.exceptions import NotFoundError, ValidationError, ConflictError
from app.utils import escapar

logger = get_logger("reserva_service")


class ReservaService:
    def __init__(self):
        self.repo = ReservaRepository()
        self.espacio_repo = EspacioRepository()
        self.notif_repo = NotificacionRepository()

    def buscar_disponibilidad(self, palabra_clave: str) -> list:
        if not palabra_clave or len(palabra_clave) > 500:
            return []
        palabra_clave = escapar(palabra_clave.strip().lower())
        tipo = self._determinar_tipo(palabra_clave)
        from app.database.connection import fetch_all
        try:
            return fetch_all(
                "SELECT e.*, t.nombre AS tipo FROM espacios_academicos e "
                "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
                "WHERE t.nombre = %s AND e.estado = 'DISPONIBLE'",
                (tipo,)
            )
        except Exception as e:
            logger.error(f"Error buscando disponibilidad: {e}")
            return []

    def crear(self, id_usuario: int, id_espacio: int, fecha: str = "2026-05-28",
              curso_nombre: str = "", horario: str = "") -> Optional[dict]:
        if not isinstance(id_usuario, int) or id_usuario <= 0:
            raise ValidationError("ID de usuario inválido")
        if not isinstance(id_espacio, int) or id_espacio <= 0:
            raise ValidationError("ID de espacio inválido")

        espacio = self.espacio_repo.get_by_id(id_espacio)
        if not espacio:
            raise NotFoundError("Espacio")

        data = {
            "id_usuario": id_usuario,
            "id_espacio": id_espacio,
            "curso_nombre": curso_nombre or "Reserva Rápida",
            "horario": horario or "08:00-10:00",
            "fecha": fecha,
        }
        reserva = self.repo.create(data)

        if reserva:
            from app.database.connection import execute
            execute(
                "UPDATE espacios_academicos SET estado = 'OCUPADO' WHERE id_espacio = %s",
                (id_espacio,)
            )
            logger.info(f"Reserva creada: espacio={id_espacio}, usuario={id_usuario}")

        return reserva

    def cancelar(self, id_reserva: int, id_usuario: int | None = None) -> bool:
        reserva = self.repo.get_by_id(id_reserva)
        if not reserva:
            raise NotFoundError("Reserva")

        if id_usuario and reserva["id_usuario"] != id_usuario:
            from app.database.connection import fetch_one
            usuario = fetch_one(
                "SELECT rol FROM usuarios WHERE id_usuario = %s", (id_usuario,)
            )
            if not usuario or usuario.get("rol") != "Admin":
                raise ValidationError("No puedes cancelar una reserva que no te pertenece")

        exito = self.repo.cancelar(id_reserva)
        if exito:
            from app.database.connection import execute
            execute(
                "UPDATE espacios_academicos SET estado = 'DISPONIBLE' "
                "FROM reservas WHERE reservas.id_reserva = %s "
                "AND reservas.id_espacio = espacios_academicos.id_espacio",
                (id_reserva,)
            )
            logger.info(f"Reserva cancelada: id={id_reserva}")
        return exito

    def listar_por_usuario(self, id_usuario: int) -> list:
        return self.repo.get_by_usuario(id_usuario)

    def listar_activas(self) -> list:
        return self.repo.get_activas()

    def listar_pendientes(self) -> list:
        return self.repo.get_pendientes()

    def aprobar(self, id_reserva: int) -> bool:
        reserva = self.repo.get_by_id(id_reserva)
        if not reserva:
            raise NotFoundError("Reserva")
        exito = self.repo.update_estado(id_reserva, "CONFIRMADA")
        if exito:
            self.notif_repo.create(
                reserva["id_usuario"],
                "Reserva Confirmada",
                f"Tu reserva ha sido aprobada.",
            )
            logger.info(f"Reserva aprobada: id={id_reserva}")
        return exito

    def rechazar(self, id_reserva: int) -> bool:
        reserva = self.repo.get_by_id(id_reserva)
        if not reserva:
            raise NotFoundError("Reserva")
        exito = self.repo.update_estado(id_reserva, "RECHAZADA")
        if exito:
            from app.database.connection import execute
            execute(
                "UPDATE espacios_academicos e SET estado = 'DISPONIBLE' "
                "FROM reservas r WHERE r.id_reserva = %s AND r.id_espacio = e.id_espacio",
                (id_reserva,)
            )
            self.notif_repo.create(
                reserva["id_usuario"],
                "Reserva Rechazada",
                f"Tu reserva ha sido rechazada.",
            )
            logger.info(f"Reserva rechazada: id={id_reserva}")
        return exito

    def obtener_historial_por_espacio(self, id_espacio: int) -> list:
        return self.repo.get_by_espacio(id_espacio)

    def _determinar_tipo(self, palabra: str) -> str:
        if "computo" in palabra or "cómputo" in palabra:
            return "SALA DE COMPUTO"
        elif "laboratorio" in palabra or "lab" in palabra:
            return "LABORATORIO"
        elif "teorica" in palabra or "teórica" in palabra or "aula" in palabra:
            return "AULA"
        return "SALA DE COMPUTO"
