"""Servicio de administración - dashboard, estadísticas, gestión."""

from app.repositories.usuario_repository import UsuarioRepository
from app.repositories.espacio_repository import EspacioRepository
from app.repositories.reserva_repository import ReservaRepository
from app.repositories.notificacion_repository import NotificacionRepository
from app.logger import get_logger
from app.database.connection import fetch_all, fetch_one

logger = get_logger("admin_service")


class AdminService:
    def __init__(self):
        self.usuario_repo = UsuarioRepository()
        self.espacio_repo = EspacioRepository()
        self.reserva_repo = ReservaRepository()
        self.notif_repo = NotificacionRepository()

    def obtener_estadisticas(self) -> dict:
        try:
            total_usuarios = self.usuario_repo.count()
            total_espacios = self.espacio_repo.count()
            reservas_activas = self.reserva_repo.count(
                "estado = 'CONFIRMADA' OR estado = '1'"
            )
            disponibles = self.espacio_repo.count("estado = 'DISPONIBLE'")
            ocupados = self.espacio_repo.count("estado != 'DISPONIBLE'")
            total_reservas = self.reserva_repo.count()
            reservas_pendientes = self.reserva_repo.count("estado = 'PENDIENTE'")
            tasa_ocupacion = round(
                (ocupados / total_espacios * 100) if total_espacios > 0 else 0, 1
            )

            por_tipo_list = fetch_all(
                "SELECT t.nombre, COUNT(*) AS total FROM espacios_academicos e "
                "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo GROUP BY t.nombre"
            )
            por_tipo = {r["nombre"]: r["total"] for r in por_tipo_list}

            return {
                "total_usuarios": total_usuarios,
                "total_espacios": total_espacios,
                "reservas_activas": reservas_activas,
                "espacios_disponibles": disponibles,
                "ocupados": ocupados,
                "por_tipo": por_tipo,
                "total_activos": total_espacios,
                "por_facultad": {},
                "total_reservas": total_reservas,
                "reservas_pendientes": reservas_pendientes,
                "tasa_ocupacion": tasa_ocupacion,
            }
        except Exception as e:
            logger.error(f"Error obteniendo estadísticas: {e}")
            return {}

    def obtener_usuarios(self) -> list:
        return fetch_all(
            "SELECT u.id_usuario, u.nombre, u.username, "
            "COALESCE(r.nombre, 'Docente') AS rol, u.estado, u.estado_int "
            "FROM usuarios u "
            "LEFT JOIN roles r ON u.id_rol = r.id_rol "
            "WHERE u.estado_int = 1 "
            "ORDER BY u.nombre"
        )

    def obtener_bloques_horario(self) -> list:
        return fetch_all(
            "SELECT bh.*, r.id_espacio, e.nombre AS espacio_nombre, t.nombre AS tipo "
            "FROM bloques_horario bh "
            "LEFT JOIN reservas r ON bh.id_bloque = r.id_bloque "
            "LEFT JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
            "LEFT JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
            "ORDER BY bh.dia_semana, bh.hora_inicio"
        )

    def obtener_facultades(self) -> list:
        try:
            ubicaciones = fetch_all(
                "SELECT DISTINCT ubicacion FROM espacios_academicos "
                "WHERE ubicacion IS NOT NULL"
            )
            resultado = []
            for u in ubicaciones:
                f = u["ubicacion"]
                total = self.espacio_repo.count("ubicacion = %s", (f,))
                reservas_count = fetch_one(
                    "SELECT COUNT(*) AS total FROM reservas r "
                    "JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
                    "WHERE e.ubicacion = %s AND r.estado = 'CONFIRMADA'",
                    (f,)
                )["total"]
                disponibles = self.espacio_repo.count(
                    "ubicacion = %s AND estado = 'DISPONIBLE'", (f,)
                )
                resultado.append({
                    "nombre": f,
                    "total_espacios": total,
                    "reservas": reservas_count,
                    "disponibles": disponibles,
                })
            return resultado
        except Exception as e:
            logger.error(f"Error obteniendo facultades: {e}")
            return []
