"""Modelos del dominio - Inicialización de base de datos."""

from app.logger import get_logger

logger = get_logger("init")


def inicializar_bd():
    try:
        from app.database.connection import init_pool, execute
        init_pool()

        migraciones = [
            "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS estado SMALLINT DEFAULT 1",
            "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS fecha_creacion TIMESTAMP DEFAULT NOW()",
            "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS fecha_actualizacion TIMESTAMP DEFAULT NOW()",
            "ALTER TABLE espacios_academicos ADD COLUMN IF NOT EXISTS fecha_creacion TIMESTAMP DEFAULT NOW()",
            "ALTER TABLE reservas ADD COLUMN IF NOT EXISTS id_curso INTEGER REFERENCES cursos(id_curso)",
            "ALTER TABLE reservas ADD COLUMN IF NOT EXISTS id_bloque INTEGER REFERENCES bloques_horario(id_bloque)",
            "ALTER TABLE reservas ADD COLUMN IF NOT EXISTS estado SMALLINT DEFAULT 1",
            "ALTER TABLE reservas ADD COLUMN IF NOT EXISTS fecha_creacion TIMESTAMP DEFAULT NOW()",
            "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS id_usuario INTEGER REFERENCES usuarios(id_usuario)",
            "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS prompt_original TEXT",
            "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS intencion_detectada VARCHAR(255)",
            "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS entidades_encontradas JSONB",
            "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS resultado_json JSONB",
            "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS modelo_usado VARCHAR(100)",
            "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS tiempo_procesamiento_ms INTEGER",
            "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS fecha_creacion TIMESTAMP DEFAULT NOW()",
            "ALTER TABLE espacios_academicos ADD COLUMN IF NOT EXISTS estado_int SMALLINT DEFAULT 1",
            "ALTER TABLE reservas ADD COLUMN IF NOT EXISTS estado_int SMALLINT DEFAULT 1",
            "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS estado_int SMALLINT DEFAULT 1",
        ]
        for sql in migraciones:
            try:
                execute(sql)
            except Exception:
                pass
        logger.info("Base de datos inicializada correctamente")
    except Exception as e:
        logger.error(f"Error inicializando base de datos: {e}")
