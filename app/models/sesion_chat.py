from config.database import Database
from core.logger import get_logger

logger = get_logger("sesion_chat")


class SesionChat:
    def __init__(self, db: Database):
        self.db = db

    def crear_tablas(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sesiones_chat (
                id_sesion SERIAL PRIMARY KEY,
                id_usuario INTEGER NOT NULL REFERENCES usuarios(id_usuario),
                titulo VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes_chat (
                id_mensaje SERIAL PRIMARY KEY,
                id_sesion INTEGER NOT NULL REFERENCES sesiones_chat(id_sesion) ON DELETE CASCADE,
                tipo VARCHAR(50) NOT NULL,
                contenido_json TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
        conn.commit()
        conn.close()

    def listar(self, id_usuario: int) -> list:
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_sesion, titulo, created_at FROM sesiones_chat WHERE id_usuario = %s ORDER BY created_at DESC LIMIT 50",
            (id_usuario,)
        )
        filas = cursor.fetchall()
        conn.close()
        return [dict(f) for f in filas]

    def crear(self, id_usuario: int, titulo: str) -> int:
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sesiones_chat (id_usuario, titulo) VALUES (%s, %s) RETURNING id_sesion",
            (id_usuario, titulo)
        )
        id_sesion = cursor.fetchone()["id_sesion"]
        conn.commit()
        conn.close()
        return id_sesion

    def obtener_mensajes(self, id_sesion: int) -> list:
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT tipo, contenido_json, created_at FROM mensajes_chat WHERE id_sesion = %s ORDER BY id_mensaje",
            (id_sesion,)
        )
        filas = cursor.fetchall()
        conn.close()
        return [dict(f) for f in filas]

    def guardar_mensaje(self, id_sesion: int, tipo: str, contenido_json: str):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO mensajes_chat (id_sesion, tipo, contenido_json) VALUES (%s, %s, %s)",
            (id_sesion, tipo, contenido_json)
        )
        conn.commit()
        conn.close()

    def eliminar(self, id_sesion: int):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sesiones_chat WHERE id_sesion = %s", (id_sesion,))
        conn.commit()
        conn.close()
