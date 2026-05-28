from config.database import Database
from .usuario import Usuario
from .docente import Docente
from .curso import Curso
from .espacio import EspacioAcademico
from .bloque_horario import BloqueHorario
from .reserva import Reserva
from .procesador_nlp import ProcesadorNLP


def _migrar_columnas(db: Database):
    conn = db.obtener_conexion()
    cursor = conn.cursor()
    migraciones = [
        "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS estado VARCHAR(50) DEFAULT 'Activo'",
        "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS fecha_creacion TIMESTAMP DEFAULT NOW()",
        "ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS fecha_actualizacion TIMESTAMP DEFAULT NOW()",
        "ALTER TABLE espacios_academicos ADD COLUMN IF NOT EXISTS fecha_creacion TIMESTAMP DEFAULT NOW()",
        "ALTER TABLE reservas ADD COLUMN IF NOT EXISTS id_curso INTEGER REFERENCES cursos(id_curso)",
        "ALTER TABLE reservas ADD COLUMN IF NOT EXISTS id_bloque INTEGER REFERENCES bloques_horario(id_bloque)",
        "ALTER TABLE reservas ADD COLUMN IF NOT EXISTS estado VARCHAR(50) DEFAULT 'Confirmada'",
        "ALTER TABLE reservas ADD COLUMN IF NOT EXISTS fecha_creacion TIMESTAMP DEFAULT NOW()",
        "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS id_usuario INTEGER REFERENCES usuarios(id_usuario)",
        "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS prompt_original TEXT",
        "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS intencion_detectada VARCHAR(255)",
        "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS entidades_encontradas JSONB",
        "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS resultado_json JSONB",
        "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS modelo_usado VARCHAR(100)",
        "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS tiempo_procesamiento_ms INTEGER",
        "ALTER TABLE procesamiento_nlp ADD COLUMN IF NOT EXISTS fecha_creacion TIMESTAMP DEFAULT NOW()",
    ]
    for sql in migraciones:
        try:
            cursor.execute(sql)
        except Exception:
            pass
    conn.commit()
    conn.close()


import bcrypt


def _migrar_passwords(db: Database):
    conn = db.obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id_usuario, password_hash FROM usuarios WHERE password_hash NOT LIKE '$2b$%'")
    for row in cursor.fetchall():
        nuevo = bcrypt.hashpw(row["password_hash"].encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        cursor.execute("UPDATE usuarios SET password_hash = %s WHERE id_usuario = %s", (nuevo, row["id_usuario"]))
    conn.commit()
    conn.close()


def inicializar_bd():
    db = Database()
    Usuario.crear_tabla(db)
    Docente.crear_tabla(db)
    Curso.crear_tabla(db)
    EspacioAcademico.crear_tabla(db)
    BloqueHorario.crear_tabla(db)
    Reserva.crear_tabla(db)
    ProcesadorNLP.crear_tabla(db)
    _migrar_columnas(db)
    _migrar_passwords(db)
    Usuario.sembrar(db)
    EspacioAcademico.sembrar(db)
