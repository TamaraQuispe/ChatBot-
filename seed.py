import bcrypt
from config.database import Database
from dotenv import load_dotenv
from app.logger import get_logger
load_dotenv()

logger = get_logger("seed")

db = Database()
conn = db.obtener_conexion()
cur = conn.cursor()

# --- 1. USUARIOS ---
logger.info("Insertando usuarios...")
pwd_docente = bcrypt.hashpw("utp123".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
pwd_admin = bcrypt.hashpw("admin123".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

usuarios_data = [
    ("C23204737", pwd_docente, "Mg. Carmen Ludeña", "c.ludena@utp.edu.pe", 2),
    ("C23204738", pwd_docente, "Ing. Juan Quispe", "j.quispe@utp.edu.pe", 2),
    ("atorres", pwd_admin, "Ing. Luis Torres", "atorres@utp.edu.pe", 1),
]
for u in usuarios_data:
    cur.execute(
        "INSERT INTO usuarios (username, password_hash, nombre, correo, id_rol) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        u
    )

# --- 2. DOCENTES ---
logger.info("Insertando docentes...")
cur.execute("SELECT id_usuario, username FROM usuarios WHERE username IN ('C23204737','C23204738')")
user_map = {r["username"]: r["id_usuario"] for r in cur.fetchall()}

docentes_data = [
    (user_map["C23204737"], "DOC003", "Ingenieria de Sistemas", "Maestria en Ingenieria de Software", "999000111", "c.ludena@utp.edu.pe"),
    (user_map["C23204738"], "DOC004", "Ingenieria de Software", "Maestria en Ciencias de la Computacion", "999000222", "j.quispe@utp.edu.pe"),
]
for d in docentes_data:
    cur.execute(
        "INSERT INTO docentes (id_usuario, codigo_docente, departamento, grado_academico, telefono, correo_institucional) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        d
    )

# --- 3. BLOQUES HORARIO ---
logger.info("Insertando bloques horario...")
bloques_data = [
    ("BLOQUE 1 - MAÑANA", "08:00", "09:30", "LUNES", "DIURNO"),
    ("BLOQUE 2 - MAÑANA", "09:45", "11:15", "LUNES", "DIURNO"),
    ("BLOQUE 3 - MAÑANA", "11:30", "13:00", "LUNES", "DIURNO"),
    ("BLOQUE 4 - TARDE", "13:00", "14:30", "LUNES", "DIURNO"),
    ("BLOQUE 5 - TARDE", "14:45", "16:15", "LUNES", "DIURNO"),
    ("BLOQUE 6 - TARDE", "16:30", "18:00", "LUNES", "DIURNO"),
    ("BLOQUE 7 - NOCHE", "18:15", "19:45", "LUNES", "NOCTURNO"),
    ("BLOQUE 8 - NOCHE", "20:00", "21:30", "LUNES", "NOCTURNO"),
]
for b in bloques_data:
    cur.execute(
        "INSERT INTO bloques_horario (nombre, hora_inicio, hora_fin, dia_semana, turno) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        b
    )

# --- 4. SOFTWARE ---
logger.info("Insertando software...")
software_data = [
    ("Windows 11 Pro", "23H2"),
    ("Visual Studio Code", "1.98"),
    ("Python 3.12", "3.12.2"),
    ("SQL Server 2022", "16.0"),
    ("Oracle SQL Developer", "23.1"),
    ("Android Studio", "2024.2"),
    ("Docker Desktop", "4.34"),
    ("PostgreSQL 16", "16.4"),
    ("Node.js 22", "22.12"),
    ("Git", "2.47"),
]
for s in software_data:
    cur.execute(
        "INSERT INTO software (nombre, version) VALUES (%s,%s) ON CONFLICT DO NOTHING",
        s
    )

# --- 5. EQUIPAMIENTOS ---
logger.info("Insertando equipamientos...")
equipamiento_data = [
    ("PC Dell OptiPlex 7090",),
    ("Proyector Epson EB-FH06",),
    ("Pizarra Digital Smart Board 75",),
    ("Router Cisco RV340",),
    ("Switch Cisco SG350",),
    ("Servidor Dell PowerEdge T140",),
    ("Camara Web Logitech C920",),
]
for e in equipamiento_data:
    cur.execute(
        "INSERT INTO equipamientos (nombre) VALUES (%s) ON CONFLICT DO NOTHING",
        e
    )

# --- 6. ESPACIOS ACADEMICOS ---
logger.info("Insertando espacios academicos (UTP Lima Norte)...")
espacios_data = [
    ("Lab. de Computo - Sistemas 1", 1, "Pabellon A - Primer Piso - Sede Lima Norte", 30),
    ("Lab. de Computo - Sistemas 2", 1, "Pabellon A - Segundo Piso - Sede Lima Norte", 25),
    ("Lab. de Ingenieria de Software", 1, "Pabellon A - Tercer Piso - Sede Lima Norte", 20),
    ("Aula 201 - Sistemas", 2, "Pabellon B - Segundo Piso - Sede Lima Norte", 40),
    ("Aula 202 - Sistemas", 2, "Pabellon B - Segundo Piso - Sede Lima Norte", 35),
    ("Auditorio de Ingenieria", 3, "Pabellon C - Sede Lima Norte", 200),
    ("Sala de Computo - Base de Datos", 1, "Pabellon A - Tercer Piso - Sede Lima Norte", 20),
    ("Lab. de Redes y Telecomunicaciones", 1, "Pabellon D - Sede Lima Norte", 15),
]
for e in espacios_data:
    cur.execute(
        "INSERT INTO espacios_academicos (nombre, id_tipo, ubicacion, capacidad) VALUES (%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        e
    )

# Get IDs for relationships
cur.execute("SELECT id_software, nombre FROM software")
sw_map = {r["nombre"]: r["id_software"] for r in cur.fetchall()}
cur.execute("SELECT id_equipamiento, nombre FROM equipamientos")
eq_map = {r["nombre"]: r["id_equipamiento"] for r in cur.fetchall()}
cur.execute("SELECT id_espacio, nombre FROM espacios_academicos")
esp_map = {r["nombre"]: r["id_espacio"] for r in cur.fetchall()}
cur.execute("SELECT id_docente, u.username FROM docentes d JOIN usuarios u ON u.id_usuario = d.id_usuario")
doc_map = {r["username"]: r["id_docente"] for r in cur.fetchall()}
cur.execute("SELECT id_bloque, nombre FROM bloques_horario")
bloq_map = {r["nombre"]: r["id_bloque"] for r in cur.fetchall()}

# --- 7. ESPACIO_SOFTWARE ---
logger.info("Insertando espacio_software...")
esp_sw_data = [
    (esp_map["Lab. de Computo - Sistemas 1"], sw_map["Windows 11 Pro"]),
    (esp_map["Lab. de Computo - Sistemas 1"], sw_map["Visual Studio Code"]),
    (esp_map["Lab. de Computo - Sistemas 1"], sw_map["Python 3.12"]),
    (esp_map["Lab. de Computo - Sistemas 1"], sw_map["SQL Server 2022"]),
    (esp_map["Lab. de Computo - Sistemas 1"], sw_map["Git"]),
    (esp_map["Lab. de Computo - Sistemas 2"], sw_map["Windows 11 Pro"]),
    (esp_map["Lab. de Computo - Sistemas 2"], sw_map["Visual Studio Code"]),
    (esp_map["Lab. de Computo - Sistemas 2"], sw_map["PostgreSQL 16"]),
    (esp_map["Lab. de Computo - Sistemas 2"], sw_map["Node.js 22"]),
    (esp_map["Lab. de Computo - Sistemas 2"], sw_map["Git"]),
    (esp_map["Lab. de Ingenieria de Software"], sw_map["Windows 11 Pro"]),
    (esp_map["Lab. de Ingenieria de Software"], sw_map["Visual Studio Code"]),
    (esp_map["Lab. de Ingenieria de Software"], sw_map["Docker Desktop"]),
    (esp_map["Lab. de Ingenieria de Software"], sw_map["Android Studio"]),
    (esp_map["Lab. de Ingenieria de Software"], sw_map["Python 3.12"]),
    (esp_map["Lab. de Ingenieria de Software"], sw_map["Git"]),
    (esp_map["Sala de Computo - Base de Datos"], sw_map["Windows 11 Pro"]),
    (esp_map["Sala de Computo - Base de Datos"], sw_map["Oracle SQL Developer"]),
    (esp_map["Sala de Computo - Base de Datos"], sw_map["SQL Server 2022"]),
    (esp_map["Sala de Computo - Base de Datos"], sw_map["PostgreSQL 16"]),
    (esp_map["Lab. de Redes y Telecomunicaciones"], sw_map["Windows 11 Pro"]),
    (esp_map["Lab. de Redes y Telecomunicaciones"], sw_map["Docker Desktop"]),
]
for es in esp_sw_data:
    cur.execute(
        "INSERT INTO espacio_software (id_espacio, id_software) VALUES (%s,%s) ON CONFLICT DO NOTHING",
        es
    )

# --- 8. ESPACIO_EQUIPAMIENTO ---
logger.info("Insertando espacio_equipamiento...")
esp_eq_data = [
    (esp_map["Lab. de Computo - Sistemas 1"], eq_map["PC Dell OptiPlex 7090"]),
    (esp_map["Lab. de Computo - Sistemas 1"], eq_map["Proyector Epson EB-FH06"]),
    (esp_map["Lab. de Computo - Sistemas 2"], eq_map["PC Dell OptiPlex 7090"]),
    (esp_map["Lab. de Computo - Sistemas 2"], eq_map["Proyector Epson EB-FH06"]),
    (esp_map["Lab. de Ingenieria de Software"], eq_map["PC Dell OptiPlex 7090"]),
    (esp_map["Lab. de Ingenieria de Software"], eq_map["Proyector Epson EB-FH06"]),
    (esp_map["Aula 201 - Sistemas"], eq_map["Proyector Epson EB-FH06"]),
    (esp_map["Aula 201 - Sistemas"], eq_map["Pizarra Digital Smart Board 75"]),
    (esp_map["Aula 202 - Sistemas"], eq_map["Proyector Epson EB-FH06"]),
    (esp_map["Auditorio de Ingenieria"], eq_map["Proyector Epson EB-FH06"]),
    (esp_map["Auditorio de Ingenieria"], eq_map["Pizarra Digital Smart Board 75"]),
    (esp_map["Sala de Computo - Base de Datos"], eq_map["PC Dell OptiPlex 7090"]),
    (esp_map["Sala de Computo - Base de Datos"], eq_map["Switch Cisco SG350"]),
    (esp_map["Lab. de Redes y Telecomunicaciones"], eq_map["PC Dell OptiPlex 7090"]),
    (esp_map["Lab. de Redes y Telecomunicaciones"], eq_map["Router Cisco RV340"]),
    (esp_map["Lab. de Redes y Telecomunicaciones"], eq_map["Switch Cisco SG350"]),
]
for ee in esp_eq_data:
    cur.execute(
        "INSERT INTO espacio_equipamiento (id_espacio, id_equipamiento) VALUES (%s,%s) ON CONFLICT DO NOTHING",
        ee
    )

# --- 9. CURSOS ---
logger.info("Insertando cursos de Ingenieria de Sistemas y Software...")
cursos_data = [
    ("SI101", "Programacion I", 4, "III", "A", 4, 2, doc_map["C23204737"], 1),
    ("SI201", "Base de Datos", 4, "IV", "A", 3, 2, doc_map["C23204738"], 1),
    ("SI301", "Estructuras de Datos", 4, "IV", "B", 3, 2, doc_map["C23204737"], 1),
    ("SI401", "Ingenieria de Software", 3, "VI", "A", 3, 2, doc_map["C23204737"], 1),
    ("SW101", "Fundamentos de Ingenieria de Software", 4, "III", "A", 3, 2, doc_map["C23204738"], 1),
    ("SW201", "Arquitectura de Software", 4, "V", "A", 3, 2, doc_map["C23204738"], 1),
    ("SI501", "Redes y Comunicaciones", 3, "V", "A", 2, 2, doc_map["C23204738"], 1),
    ("SI601", "Inteligencia Artificial", 4, "VII", "A", 3, 2, doc_map["C23204737"], 1),
]
for c in cursos_data:
    cur.execute(
        "INSERT INTO cursos (codigo, nombre, creditos, ciclo, seccion, horas_teoria, horas_practica, id_docente, id_tipo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        c
    )

# --- 10. RESERVAS ---
logger.info("Insertando reservas...")
cur.execute("SELECT id_usuario, username FROM usuarios WHERE username IN ('C23204737','C23204738')")
usr_map = {r["username"]: r["id_usuario"] for r in cur.fetchall()}
cur.execute("SELECT id_curso, codigo FROM cursos")
cur_map = {r["codigo"]: r["id_curso"] for r in cur.fetchall()}

reservas_data = [
    (usr_map["C23204737"], cur_map["SI101"], esp_map["Lab. de Computo - Sistemas 1"], bloq_map["BLOQUE 2 - MAÑANA"], "2026-07-10", "CONFIRMADA"),
    (usr_map["C23204737"], cur_map["SI301"], esp_map["Lab. de Computo - Sistemas 1"], bloq_map["BLOQUE 5 - TARDE"], "2026-07-10", "CONFIRMADA"),
    (usr_map["C23204738"], cur_map["SW101"], esp_map["Lab. de Ingenieria de Software"], bloq_map["BLOQUE 3 - MAÑANA"], "2026-07-11", "CONFIRMADA"),
    (usr_map["C23204738"], cur_map["SI501"], esp_map["Lab. de Redes y Telecomunicaciones"], bloq_map["BLOQUE 6 - TARDE"], "2026-07-14", "PENDIENTE"),
    (usr_map["C23204737"], cur_map["SI601"], esp_map["Sala de Computo - Base de Datos"], bloq_map["BLOQUE 4 - TARDE"], "2026-07-15", "PENDIENTE"),
    (usr_map["C23204738"], cur_map["SW201"], esp_map["Lab. de Ingenieria de Software"], bloq_map["BLOQUE 1 - MAÑANA"], "2026-07-16", "CONFIRMADA"),
]
for r in reservas_data:
    cur.execute(
        "INSERT INTO reservas (id_usuario, id_curso, id_espacio, id_bloque, fecha, estado) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        r
    )

# --- 11. PROCESAMIENTO_NLP ---
logger.info("Insertando procesamiento_nlp...")
nlp_data = [
    (usr_map["C23204737"], "Quiero reservar el laboratorio de sistemas para el lunes", "RESERVAR_ESPACIO", '{"intencion": "reserva", "entidad": "laboratorio sistemas"}', '{"accion": "buscar_espacio", "params": {}}', "gpt-4o-mini", 450),
    (usr_map["C23204737"], "Que cursos tengo esta semana en Ingenieria de Sistemas?", "CONSULTAR_HORARIO", '{"intencion": "horario", "periodo": "semanal", "carrera": "sistemas"}', '{"accion": "listar_cursos", "params": {}}', "gpt-4o-mini", 320),
    (usr_map["C23204738"], "Muestra las reservas del laboratorio de software", "CONSULTAR_RESERVAS", '{"intencion": "reservas", "espacio": "Lab. de Ingenieria de Software"}', '{"accion": "listar_reservas", "params": {"espacio": "Lab. de Ingenieria de Software"}}', "gpt-4o-mini", 510),
    (usr_map["C23204738"], "Agenda el aula 201 para la clase de Arquitectura de Software", "RESERVAR_ESPACIO", '{"intencion": "reserva", "espacio": "Aula 201 - Sistemas", "curso": "Arquitectura de Software"}', '{"accion": "crear_reserva", "params": {"espacio": "Aula 201 - Sistemas"}}', "gpt-4o-mini", 380),
]
for n in nlp_data:
    cur.execute(
        "INSERT INTO procesamiento_nlp (id_usuario, prompt_original, intencion_detectada, entidades_encontradas, resultado_json, modelo_usado, tiempo_procesamiento_ms) VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        n
    )

conn.commit()
cur.close()
conn.close()
logger.info("Seed completado exitosamente - UTP Lima Norte | Sistemas y Software!")
