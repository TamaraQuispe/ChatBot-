from typing import Optional
from config.database import Database
from core.logger import get_logger

logger = get_logger("reserva")

ESTADOS_RESERVA = {1: "Confirmada", 2: "Cancelada", 3: "Rechazada", 4: "Pendiente"}
ESTADOS_RESERVA_REV = {"Confirmada": 1, "Cancelada": 2, "Rechazada": 3, "Pendiente": 4}


class Reserva:
    def __init__(self, db: Database):
        self.db = db

    def crear(self, id_usuario: int, id_espacio: int, fecha: str = "2026-05-28") -> bool:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT MIN(id_curso) AS v FROM cursos")
            id_curso = cursor.fetchone()["v"] or 6
            cursor.execute("SELECT MIN(id_bloque) AS v FROM bloques_horario")
            id_bloque = cursor.fetchone()["v"] or 34
            cursor.execute(
                "INSERT INTO reservas (id_usuario, id_curso, id_espacio, id_bloque, fecha, estado) VALUES (%s, %s, %s, %s, %s, 'CONFIRMADA')",
                (id_usuario, id_curso, id_espacio, id_bloque, fecha)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            logger.error(f"Error creando reserva: {e}")
            return False

    def listar_por_usuario(self, id_usuario: int) -> list:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT r.*, e.nombre AS espacio_nombre, t.nombre AS tipo, e.ubicacion, COALESCE(c.nombre, '') AS curso_nombre "
                "FROM reservas r "
                "JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
                "JOIN tipos_espacio t ON e.id_tipo = t.id_tipo "
                "LEFT JOIN cursos c ON r.id_curso = c.id_curso "
                "WHERE r.id_usuario = %s ORDER BY r.fecha DESC",
                (id_usuario,)
            )
            filas = cursor.fetchall()
            conn.close()
            return [dict(f) for f in filas]
        except Exception as e:
            logger.error(f"Error listando reservas por usuario: {e}")
            return []

    @staticmethod
    def crear_tabla(db: Database):
        try:
            conn = db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservas (
                    id_reserva SERIAL PRIMARY KEY,
                    id_usuario INTEGER NOT NULL,
                    id_curso INTEGER,
                    curso_nombre VARCHAR(255) NOT NULL,
                    id_espacio INTEGER NOT NULL,
                    id_bloque INTEGER,
                    horario VARCHAR(100) NOT NULL,
                    fecha DATE NOT NULL,
                    estado SMALLINT NOT NULL DEFAULT 1,
                    fecha_creacion TIMESTAMP DEFAULT NOW(),
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
                    FOREIGN KEY (id_espacio) REFERENCES espacios_academicos(id_espacio),
                    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
                    FOREIGN KEY (id_bloque) REFERENCES bloques_horario(id_bloque)
                );
            """)
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Error creando tabla reservas: {e}")
