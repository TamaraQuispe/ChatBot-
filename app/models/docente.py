from config.database import Database


class Docente:
    def __init__(self, db: Database):
        self.db = db

    @staticmethod
    def crear_tabla(db: Database):
        conn = db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS docentes (
                id_docente SERIAL PRIMARY KEY,
                id_usuario INTEGER NOT NULL UNIQUE,
                especialidad VARCHAR(255),
                departamento VARCHAR(255),
                grado_academico VARCHAR(100),
                telefono VARCHAR(50),
                fecha_creacion TIMESTAMP DEFAULT NOW(),
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
            );
        """)
        conn.commit()
        conn.close()

    def listar_todos(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.*, u.nombre, u.correo, u.username
            FROM docentes d
            JOIN usuarios u ON d.id_usuario = u.id_usuario
            ORDER BY d.id_docente
        """)
        filas = cursor.fetchall()
        conn.close()
        return [dict(f) for f in filas]
