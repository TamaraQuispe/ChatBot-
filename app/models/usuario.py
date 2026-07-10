import bcrypt
from typing import Optional
from config.database import Database
from core.logger import get_logger

logger = get_logger("usuario")


class Usuario:
    def __init__(self, db: Database):
        self.db = db

    def login(self, username: str, password_plano: str) -> Optional[dict]:
        conn = None
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
            usuario = cursor.fetchone()
            if not usuario:
                logger.info(f"Usuario no encontrado: {username}")
                return None

            if not bcrypt.checkpw(
                password_plano.encode("utf-8"),
                usuario["password_hash"].encode("utf-8")
            ):
                logger.info(f"Password incorrecto para: {username}")
                return None

            columnas = [desc[0] for desc in cursor.description]
            logger.info(f"Columnas disponibles en usuarios: {columnas}")

            rol = "Docente"
            if "rol" in columnas and usuario.get("rol"):
                rol = usuario["rol"]
                logger.info(f"Rol obtenido de columna 'rol': {rol}")
            elif "id_rol" in columnas and usuario.get("id_rol"):
                try:
                    cursor.execute("SELECT nombre FROM roles WHERE id_rol = %s", (usuario["id_rol"],))
                    r = cursor.fetchone()
                    rol = r["nombre"] if r else "Docente"
                    logger.info(f"Rol obtenido de tabla roles: {rol}")
                except Exception:
                    logger.warning("No se pudo consultar tabla roles, usando default")
                    rol = "Docente"

            return {
                "id_usuario": usuario["id_usuario"],
                "username": usuario["username"],
                "rol": rol,
                "nombre": usuario["nombre"],
                "correo": usuario["correo"]
            }
        except Exception as e:
            logger.error(f"Error en login: {e}", exc_info=True)
            return None
        finally:
            if conn:
                conn.close()

    @staticmethod
    def crear_tabla(db: Database):
        try:
            conn = db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id_usuario SERIAL PRIMARY KEY,
                    username VARCHAR(255) NOT NULL UNIQUE,
                    password_hash VARCHAR(255) NOT NULL,
                    rol VARCHAR(50) NOT NULL DEFAULT 'Docente',
                    nombre VARCHAR(255) NOT NULL,
                    correo VARCHAR(255) NOT NULL UNIQUE,
                    estado SMALLINT NOT NULL DEFAULT 1,
                    fecha_creacion TIMESTAMP DEFAULT NOW(),
                    fecha_actualizacion TIMESTAMP DEFAULT NOW()
                );
            """)
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Error creando tabla usuarios: {e}")

    @staticmethod
    def sembrar(db: Database):
        try:
            conn = db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) AS count FROM usuarios;")
            if cursor.fetchone()["count"] > 0:
                conn.close()
                return
            pwd = bcrypt.hashpw("utp123".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            pwd_admin = bcrypt.hashpw("admin123".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            usuarios = [
                ("obaylon", pwd, "Docente", "Ing. Omara Baylon", "obaylon@utp.edu.pe"),
                ("jpalma", pwd, "Docente", "Dr. Ricardo Palma", "jpalma@utp.edu.pe"),
                ("atorres", pwd_admin, "Admin", "Ing. Luis Torres", "atorres@utp.edu.pe"),
            ]
            for u in usuarios:
                cursor.execute(
                    "INSERT INTO usuarios (username, password_hash, rol, nombre, correo) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (username) DO NOTHING",
                    u
                )
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Error sembrando usuarios: {e}")
