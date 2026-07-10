from config.database import Database


class BloqueHorario:
    def __init__(self, db: Database):
        self.db = db

    @staticmethod
    def crear_tabla(db: Database):
        conn = db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bloques_horario (
                id_bloque SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                hora_inicio TIME NOT NULL,
                hora_fin TIME NOT NULL,
                dia_semana VARCHAR(20) NOT NULL,
                turno VARCHAR(50) NOT NULL DEFAULT 'Diurno',
                fecha_creacion TIMESTAMP DEFAULT NOW()
            );
        """)
        conn.commit()
        conn.close()
