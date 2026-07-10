from config.database import Database


class Curso:
    def __init__(self, db: Database):
        self.db = db

    @staticmethod
    def crear_tabla(db: Database):
        conn = db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cursos (
                id_curso SERIAL PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                ciclo VARCHAR(50) NOT NULL,
                tipo_espacio_requerido VARCHAR(100),
                id_docente INTEGER,
                fecha_creacion TIMESTAMP DEFAULT NOW(),
                FOREIGN KEY (id_docente) REFERENCES docentes(id_docente)
            );
        """)
        conn.commit()
        conn.close()
