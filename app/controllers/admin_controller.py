from typing import Optional
from config.database import Database
from app.models.docente import Docente
from app.models.reserva import Reserva
from app.models.espacio import EspacioAcademico
from app.models.usuario import Usuario
from core.logger import get_logger

logger = get_logger("admin")


class AdminController:
    def __init__(self, db: Database):
        self.db = db
        self.docente_model = Docente(db)
        self.reserva_model = Reserva(db)
        self.espacio_model = EspacioAcademico(db)
        self.usuario_model = Usuario(db)

    def obtener_docentes(self) -> list:
        try:
            return self.docente_model.listar_todos()
        except Exception as e:
            logger.error(f"Error obteniendo docentes: {e}")
            return []

    def obtener_espacios(self) -> list:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT e.*, t.nombre AS tipo_nombre "
                "FROM espacios_academicos e "
                "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
                "ORDER BY e.id_espacio"
            )
            filas = cursor.fetchall()
            result = []
            for f in filas:
                d = dict(f)
                d["tipo"] = d.pop("tipo_nombre", "")
                id_esp = d["id_espacio"]
                cursor.execute(
                    "SELECT eq.nombre FROM espacio_equipamiento ee "
                    "JOIN equipamientos eq ON ee.id_equipamiento = eq.id_equipamiento "
                    "WHERE ee.id_espacio = %s", (id_esp,)
                )
                equipos = [r["nombre"] for r in cursor.fetchall()]
                cursor.execute(
                    "SELECT s.nombre FROM espacio_software es "
                    "JOIN software s ON es.id_software = s.id_software "
                    "WHERE es.id_espacio = %s", (id_esp,)
                )
                softwares = [r["nombre"] for r in cursor.fetchall()]
                d["equipamiento"] = ", ".join(equipos) if equipos else ""
                d["software"] = ", ".join(softwares) if softwares else "Ninguno"
                result.append(d)
            conn.close()
            return result
        except Exception as e:
            logger.error(f"Error obteniendo espacios: {e}")
            return []

    def obtener_reservas(self) -> list:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT r.*, e.nombre AS espacio_nombre, t.nombre AS tipo, "
                "u.nombre AS usuario_nombre, u.username "
                "FROM reservas r "
                "JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
                "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
                "JOIN usuarios u ON r.id_usuario = u.id_usuario "
                "ORDER BY r.fecha DESC"
            )
            filas = cursor.fetchall()
            conn.close()
            return [dict(f) for f in filas]
        except Exception as e:
            logger.error(f"Error obteniendo reservas: {e}")
            return []

    def aprobar_reserva(self, id_reserva: int) -> bool:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE reservas SET estado = 'CONFIRMADA' WHERE id_reserva = %s",
                (id_reserva,)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            logger.error(f"Error aprobando reserva: {e}")
            return False

    def rechazar_reserva(self, id_reserva: int) -> bool:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE reservas SET estado = 'RECHAZADA' WHERE id_reserva = %s",
                (id_reserva,)
            )
            conn.commit()
            conn.close()
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE espacios_academicos e SET estado = 'DISPONIBLE' "
                "FROM reservas r WHERE r.id_reserva = %s AND r.id_espacio = e.id_espacio",
                (id_reserva,)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            logger.error(f"Error rechazando reserva: {e}")
            return False

    def obtener_estadisticas(self) -> dict:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) AS total FROM usuarios")
            total_usuarios = cursor.fetchone()["total"]
            cursor.execute("SELECT COUNT(*) AS total FROM espacios_academicos")
            total_espacios = cursor.fetchone()["total"]
            cursor.execute("SELECT COUNT(*) AS total FROM reservas WHERE estado = 'CONFIRMADA'")
            reservas_activas = cursor.fetchone()["total"]
            cursor.execute(
                "SELECT COUNT(*) AS total FROM espacios_academicos WHERE estado = 'DISPONIBLE'"
            )
            disponibles = cursor.fetchone()["total"]
            cursor.execute(
                "SELECT t.nombre, COUNT(*) AS total FROM espacios_academicos e "
                "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo GROUP BY t.nombre"
            )
            por_tipo = {r["nombre"]: r["total"] for r in cursor.fetchall()}
            cursor.execute(
                "SELECT COUNT(*) AS total FROM espacios_academicos WHERE estado != 'DISPONIBLE'"
            )
            ocupados = cursor.fetchone()["total"]
            cursor.execute("SELECT COUNT(*) AS total FROM equipamientos")
            total_activos = cursor.fetchone()["total"]
            cursor.execute("SELECT COUNT(*) AS total FROM reservas")
            total_reservas = cursor.fetchone()["total"]
            cursor.execute(
                "SELECT COUNT(*) AS total FROM reservas WHERE estado = 'PENDIENTE'"
            )
            reservas_pendientes = cursor.fetchone()["total"]
            conn.close()
            tasa_ocupacion = round((ocupados / total_espacios * 100) if total_espacios > 0 else 0, 1)
            return {
                "total_usuarios": total_usuarios,
                "total_espacios": total_espacios,
                "reservas_activas": reservas_activas,
                "espacios_disponibles": disponibles,
                "ocupados": ocupados,
                "por_tipo": por_tipo,
                "total_activos": total_activos,
                "por_facultad": {},
                "total_reservas": total_reservas,
                "reservas_pendientes": reservas_pendientes,
                "tasa_ocupacion": tasa_ocupacion,
            }
        except Exception as e:
            logger.error(f"Error obteniendo estadisticas: {e}")
            return {}

    def obtener_activos(self) -> list:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT e.id_espacio, e.nombre, t.nombre AS tipo, e.estado "
                "FROM espacios_academicos e "
                "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
                "ORDER BY e.nombre"
            )
            espacios = cursor.fetchall()
            resultados = []
            for e in espacios:
                d = dict(e)
                id_esp = d["id_espacio"]
                cursor.execute(
                    "SELECT eq.nombre FROM espacio_equipamiento ee "
                    "JOIN equipamientos eq ON ee.id_equipamiento = eq.id_equipamiento "
                    "WHERE ee.id_espacio = %s",
                    (id_esp,)
                )
                equipos = [r["nombre"] for r in cursor.fetchall()]
                cursor.execute(
                    "SELECT s.nombre, s.version FROM espacio_software es "
                    "JOIN software s ON es.id_software = s.id_software "
                    "WHERE es.id_espacio = %s",
                    (id_esp,)
                )
                softwares = [f"{r['nombre']} {r['version'] or ''}".strip() for r in cursor.fetchall()]
                d["equipamiento"] = ", ".join(equipos) if equipos else ""
                d["software"] = ", ".join(softwares) if softwares else ""
                resultados.append(d)
            conn.close()
            return resultados
        except Exception as e:
            logger.error(f"Error obteniendo activos: {e}")
            return []

    def obtener_usuarios(self) -> list:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT u.id_usuario, u.nombre, u.username, r.nombre AS rol, u.estado "
                "FROM usuarios u JOIN roles r ON u.id_rol = r.id_rol ORDER BY u.nombre"
            )
            filas = cursor.fetchall()
            conn.close()
            return [dict(f) for f in filas]
        except Exception as e:
            logger.error(f"Error obteniendo usuarios: {e}")
            return []

    def obtener_bloques_horario(self) -> list:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT bh.*, r.id_espacio, e.nombre AS espacio_nombre, t.nombre AS tipo "
                "FROM bloques_horario bh "
                "LEFT JOIN reservas r ON bh.id_bloque = r.id_bloque "
                "LEFT JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
                "LEFT JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
                "ORDER BY bh.dia_semana, bh.hora_inicio"
            )
            filas = cursor.fetchall()
            conn.close()
            return [dict(f) for f in filas]
        except Exception as e:
            logger.error(f"Error obteniendo bloques horario: {e}")
            return []

    def obtener_facultades(self) -> list:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT ubicacion FROM espacios_academicos WHERE ubicacion IS NOT NULL")
            facultades_raw = [r["ubicacion"] for r in cursor.fetchall()]
            resultado = []
            for f in facultades_raw:
                cursor.execute(
                    "SELECT COUNT(*) AS total FROM espacios_academicos WHERE ubicacion = %s",
                    (f,)
                )
                total_espacios = cursor.fetchone()["total"]
                cursor.execute(
                    "SELECT COUNT(*) AS total FROM reservas r "
                    "JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
                    "WHERE e.ubicacion = %s AND r.estado = 'CONFIRMADA'",
                    (f,)
                )
                reservas = cursor.fetchone()["total"]
                cursor.execute(
                    "SELECT COUNT(*) AS total FROM espacios_academicos "
                    "WHERE ubicacion = %s AND estado = 'DISPONIBLE'",
                    (f,)
                )
                disponibles = cursor.fetchone()["total"]
                resultado.append({
                    "nombre": f,
                    "total_espacios": total_espacios,
                    "reservas": reservas,
                    "disponibles": disponibles,
                })
            conn.close()
            return resultado
        except Exception as e:
            logger.error(f"Error obteniendo facultades: {e}")
            return []
