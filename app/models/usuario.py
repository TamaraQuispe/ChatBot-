import bcrypt
from config.database import Database


class Usuario:
    def __init__(self, db: Database):
        self.db = db

    def login(self, username: str, password_plano: str):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            """SELECT u.*, r.nombre AS rol_nombre
               FROM usuarios u
               JOIN roles r ON r.id_rol = u.id_rol
               WHERE u.username = %s""",
            (username,)
        )
        usuario = cursor.fetchone()
        conn.close()
        if usuario and bcrypt.checkpw(
            password_plano.encode("utf-8"),
            usuario["password_hash"].encode("utf-8")
        ):
            return {
                "id_usuario": usuario["id_usuario"],
                "username": usuario["username"],
                "rol": usuario["rol_nombre"],
                "nombre": usuario["nombre"],
                "correo": usuario["correo"]
            }
        return None

    @staticmethod
    def crear_tabla(db: Database):
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
                estado VARCHAR(50) NOT NULL DEFAULT 'Activo',
                fecha_creacion TIMESTAMP DEFAULT NOW(),
                fecha_actualizacion TIMESTAMP DEFAULT NOW()
            );
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def sembrar(db: Database):
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
