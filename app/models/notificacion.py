from config.database import Database
from core.logger import get_logger

logger = get_logger("notificacion")


class Notificacion:
    def __init__(self, db: Database):
        self.db = db

    def crear_tabla(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notificaciones (
                id_notificacion SERIAL PRIMARY KEY,
                id_usuario INTEGER NOT NULL REFERENCES usuarios(id_usuario),
                titulo VARCHAR(255) NOT NULL,
                mensaje TEXT NOT NULL,
                tipo VARCHAR(50) NOT NULL DEFAULT 'info',
                leida BOOLEAN NOT NULL DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
        conn.commit()
        conn.close()

    def crear(self, id_usuario: int, titulo: str, mensaje: str, tipo: str = "info"):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO notificaciones (id_usuario, titulo, mensaje, tipo) VALUES (%s, %s, %s, %s)",
            (id_usuario, titulo, mensaje, tipo)
        )
        conn.commit()
        conn.close()

    def listar(self, id_usuario: int, limite: int = 20) -> list:
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_notificacion, titulo, mensaje, tipo, leida, created_at "
            "FROM notificaciones WHERE id_usuario = %s ORDER BY created_at DESC LIMIT %s",
            (id_usuario, limite)
        )
        filas = cursor.fetchall()
        conn.close()
        return [dict(f) for f in filas]

    def contar_no_leidas(self, id_usuario: int) -> int:
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT COUNT(*) AS total FROM notificaciones WHERE id_usuario = %s AND leida = FALSE",
            (id_usuario,)
        )
        total = cursor.fetchone()["total"]
        conn.close()
        return total

    def marcar_leida(self, id_notificacion: int):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE notificaciones SET leida = TRUE WHERE id_notificacion = %s",
            (id_notificacion,)
        )
        conn.commit()
        conn.close()

    def marcar_todas_leidas(self, id_usuario: int):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE notificaciones SET leida = TRUE WHERE id_usuario = %s AND leida = FALSE",
            (id_usuario,)
        )
        conn.commit()
        conn.close()
