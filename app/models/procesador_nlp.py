from config.database import Database


class ProcesadorNLP:
    def __init__(self, db: Database):
        self.db = db

    @staticmethod
    def crear_tabla(db: Database):
        conn = db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS procesamiento_nlp (
                id_procesamiento SERIAL PRIMARY KEY,
                id_usuario INTEGER NOT NULL,
                prompt_original TEXT NOT NULL,
                intencion_detectada VARCHAR(255),
                entidades_encontradas JSONB,
                resultado_json JSONB,
                modelo_usado VARCHAR(100),
                tiempo_procesamiento_ms INTEGER,
                fecha_creacion TIMESTAMP DEFAULT NOW(),
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
            );
        """)
        conn.commit()
        conn.close()
