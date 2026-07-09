from typing import Optional
from config.database import Database
from .interfaces import IGestorReservas
from .reserva import Reserva
from .espacio import EspacioAcademico
from core.logger import get_logger

logger = get_logger("gestor_reservas")


class GestorReservas(IGestorReservas):
    def __init__(self, db: Database):
        self.db = db
        self.reserva_model = Reserva(db)
        self.espacio_model = EspacioAcademico(db)

    def crear_reserva(self, id_usuario: int, id_espacio: int, curso_nombre: str, horario: str, fecha: str = "2026-05-28") -> bool:
        try:
            exito = self.reserva_model.crear(id_usuario, curso_nombre, id_espacio, horario, fecha)
            if exito:
                self.espacio_model.ocupar(id_espacio)
                logger.info(f"Reserva creada: espacio={id_espacio}, usuario={id_usuario}")
            return exito
        except Exception as e:
            logger.error(f"Error al crear reserva: {e}")
            return False

    def cancelar_reserva(self, id_reserva: int) -> bool:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE reservas SET estado = 'Cancelada' WHERE id_reserva = %s",
                (id_reserva,)
            )
            conn.commit()
            conn.close()
            logger.info(f"Reserva cancelada: id={id_reserva}")
            return True
        except Exception as e:
            logger.error(f"Error al cancelar reserva: {e}")
            return False

    def listar_reservas_activas(self) -> list:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT r.*, e.nombre AS espacio_nombre, e.tipo, u.nombre AS usuario_nombre "
                "FROM reservas r "
                "JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
                "JOIN usuarios u ON r.id_usuario = u.id_usuario "
                "WHERE r.estado = 'Confirmada' ORDER BY r.fecha DESC"
            )
            filas = cursor.fetchall()
            conn.close()
            return [dict(f) for f in filas]
        except Exception as e:
            logger.error(f"Error listando reservas activas: {e}")
            return []

    def reservas_por_usuario(self, id_usuario: int) -> list:
        return self.reserva_model.listar_por_usuario(id_usuario)
