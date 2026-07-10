from typing import Optional
from config.database import Database
from core.logger import get_logger

logger = get_logger("reserva")

ESTADOS_RESERVA = {1: "Confirmada", 2: "Cancelada", 3: "Rechazada", 4: "Pendiente"}
ESTADOS_RESERVA_REV = {"Confirmada": 1, "Cancelada": 2, "Rechazada": 3, "Pendiente": 4}


class Reserva:
    def __init__(self, db: Database):
        self.db = db

    def crear(self, id_usuario: int, curso_nombre: str, id_espacio: int, horario: str, fecha: str = "2026-05-28") -> bool:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO reservas (id_usuario, curso_nombre, id_espacio, horario, fecha, estado) VALUES (%s, %s, %s, %s, %s, 1)",
                (id_usuario, curso_nombre, id_espacio, horario, fecha)
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
                "SELECT r.*, e.nombre AS espacio_nombre, e.tipo, e.ubicacion "
                "FROM reservas r "
                "JOIN espacios_academicos e ON r.id_espacio = e.id_espacio "
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
