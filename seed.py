import bcrypt
from config.database import Database
from dotenv import load_dotenv
load_dotenv()

db = Database()
conn = db.obtener_conexion()
cur = conn.cursor()

# --- 1. USUARIOS ---
print("Insertando usuarios...")
pwd_docente = bcrypt.hashpw("utp123".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
pwd_admin = bcrypt.hashpw("admin123".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

usuarios_data = [
    ("obaylon", pwd_docente, "Ing. Omara Baylon", "obaylon@utp.edu.pe", 2),
    ("jpalma", pwd_docente, "Dr. Ricardo Palma", "jpalma@utp.edu.pe", 2),
    ("atorres", pwd_admin, "Ing. Luis Torres", "atorres@utp.edu.pe", 1),
]
for u in usuarios_data:
    cur.execute(
        "INSERT INTO usuarios (username, password_hash, nombre, correo, id_rol) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        u
    )

# --- 2. DOCENTES ---
print("Insertando docentes...")
cur.execute("SELECT id_usuario, username FROM usuarios WHERE username IN ('obaylon','jpalma')")
user_map = {r["username"]: r["id_usuario"] for r in cur.fetchall()}

docentes_data = [
    (user_map["obaylon"], "DOC001", "Ingenieria de Sistemas", "Maestria en Ingenieria de Software", "999111222", "obaylon@utp.edu.pe"),
    (user_map["jpalma"], "DOC002", "Ingenieria Civil", "Doctorado en Estructuras", "999333444", "jpalma@utp.edu.pe"),
]
for d in docentes_data:
    cur.execute(
        "INSERT INTO docentes (id_usuario, codigo_docente, departamento, grado_academico, telefono, correo_institucional) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        d
    )

# --- 3. BLOQUES HORARIO ---
print("Insertando bloques horario...")
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
print("Insertando software...")
software_data = [
    ("Windows 11 Pro", "23H2"),
    ("Visual Studio Code", "1.98"),
    ("AutoCAD 2024", "24.3"),
    ("MATLAB R2024a", "R2024a"),
    ("Python 3.12", "3.12.2"),
    ("SolidWorks 2024", "SP2"),
    ("Adobe Creative Cloud", "2024"),
]
for s in software_data:
    cur.execute(
        "INSERT INTO software (nombre, version) VALUES (%s,%s) ON CONFLICT DO NOTHING",
        s
    )

# --- 5. EQUIPAMIENTOS ---
print("Insertando equipamientos...")
equipamiento_data = [
    ("Proyector Epson EB-FH06",),
    ("PC Dell OptiPlex 7080",),
    ("Impresora 3D Creality Ender-3",),
    ("Pizarra Digital Smart Board 75",),
    ("Router Cisco RV340",),
    ("Camara Documental Epson ELPDC30",),
    ("Microscopio Digital Celestron",),
]
for e in equipamiento_data:
    cur.execute(
        "INSERT INTO equipamientos (nombre) VALUES (%s) ON CONFLICT DO NOTHING",
        e
    )

# --- 6. ESPACIOS ACADEMICOS ---
print("Insertando espacios academicos...")
espacios_data = [
    ("Laboratorio de Computo 1", 1, "Pabellon A - Primer Piso", 30),
    ("Laboratorio de Computo 2", 1, "Pabellon A - Segundo Piso", 25),
    ("Aula 101", 2, "Pabellon B - Primer Piso", 40),
    ("Aula 102", 2, "Pabellon B - Primer Piso", 35),
    ("Auditorio Principal", 3, "Pabellon C", 200),
    ("Sala de Computo 1", 4, "Pabellon A - Tercer Piso", 20),
    ("Taller de Electronica", 5, "Pabellon D", 15),
    ("Laboratorio de Fisica", 1, "Pabellon E", 20),
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
print("Insertando espacio_software...")
esp_sw_data = [
    (esp_map["Laboratorio de Computo 1"], sw_map["Windows 11 Pro"]),
    (esp_map["Laboratorio de Computo 1"], sw_map["Visual Studio Code"]),
    (esp_map["Laboratorio de Computo 1"], sw_map["Python 3.12"]),
    (esp_map["Laboratorio de Computo 2"], sw_map["Windows 11 Pro"]),
    (esp_map["Laboratorio de Computo 2"], sw_map["AutoCAD 2024"]),
    (esp_map["Laboratorio de Computo 2"], sw_map["SolidWorks 2024"]),
    (esp_map["Sala de Computo 1"], sw_map["Windows 11 Pro"]),
    (esp_map["Sala de Computo 1"], sw_map["MATLAB R2024a"]),
    (esp_map["Sala de Computo 1"], sw_map["Visual Studio Code"]),
    (esp_map["Laboratorio de Fisica"], sw_map["MATLAB R2024a"]),
    (esp_map["Auditorio Principal"], sw_map["Windows 11 Pro"]),
]
for es in esp_sw_data:
    cur.execute(
        "INSERT INTO espacio_software (id_espacio, id_software) VALUES (%s,%s) ON CONFLICT DO NOTHING",
        es
    )

# --- 8. ESPACIO_EQUIPAMIENTO ---
print("Insertando espacio_equipamiento...")
esp_eq_data = [
    (esp_map["Laboratorio de Computo 1"], eq_map["PC Dell OptiPlex 7080"]),
    (esp_map["Laboratorio de Computo 1"], eq_map["Proyector Epson EB-FH06"]),
    (esp_map["Laboratorio de Computo 2"], eq_map["PC Dell OptiPlex 7080"]),
    (esp_map["Laboratorio de Computo 2"], eq_map["Proyector Epson EB-FH06"]),
    (esp_map["Aula 101"], eq_map["Proyector Epson EB-FH06"]),
    (esp_map["Aula 101"], eq_map["Pizarra Digital Smart Board 75"]),
    (esp_map["Auditorio Principal"], eq_map["Proyector Epson EB-FH06"]),
    (esp_map["Auditorio Principal"], eq_map["Camara Documental Epson ELPDC30"]),
    (esp_map["Taller de Electronica"], eq_map["Impresora 3D Creality Ender-3"]),
    (esp_map["Taller de Electronica"], eq_map["Microscopio Digital Celestron"]),
    (esp_map["Sala de Computo 1"], eq_map["PC Dell OptiPlex 7080"]),
    (esp_map["Sala de Computo 1"], eq_map["Router Cisco RV340"]),
]
for ee in esp_eq_data:
    cur.execute(
        "INSERT INTO espacio_equipamiento (id_espacio, id_equipamiento) VALUES (%s,%s) ON CONFLICT DO NOTHING",
        ee
    )

# --- 9. CURSOS ---
print("Insertando cursos...")
cursos_data = [
    ("CS101", "Programacion I", 4, "III", "A", 4, 2, doc_map["obaylon"], 1),
    ("CS201", "Base de Datos", 4, "IV", "A", 3, 2, doc_map["obaylon"], 1),
    ("CS301", "Estructuras de Datos", 4, "IV", "B", 3, 2, doc_map["jpalma"], 1),
    ("CS401", "Ingenieria de Software", 3, "VI", "A", 3, 2, doc_map["obaylon"], 1),
    ("CE102", "Resistencia de Materiales", 5, "IV", "A", 3, 4, doc_map["jpalma"], 2),
]
for c in cursos_data:
    cur.execute(
        "INSERT INTO cursos (codigo, nombre, creditos, ciclo, seccion, horas_teoria, horas_practica, id_docente, id_tipo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        c
    )

# --- 10. RESERVAS ---
print("Insertando reservas...")
cur.execute("SELECT id_usuario, username FROM usuarios WHERE username IN ('obaylon','jpalma')")
usr_map = {r["username"]: r["id_usuario"] for r in cur.fetchall()}
cur.execute("SELECT id_curso, codigo FROM cursos")
cur_map = {r["codigo"]: r["id_curso"] for r in cur.fetchall()}

reservas_data = [
    (usr_map["obaylon"], cur_map["CS101"], esp_map["Laboratorio de Computo 1"], bloq_map["BLOQUE 2 - MAÑANA"], "2026-07-10", "CONFIRMADA"),
    (usr_map["obaylon"], cur_map["CS201"], esp_map["Sala de Computo 1"], bloq_map["BLOQUE 4 - TARDE"], "2026-07-10", "CONFIRMADA"),
    (usr_map["jpalma"], cur_map["CS301"], esp_map["Aula 101"], bloq_map["BLOQUE 3 - MAÑANA"], "2026-07-11", "PENDIENTE"),
    (usr_map["obaylon"], cur_map["CS401"], esp_map["Laboratorio de Computo 2"], bloq_map["BLOQUE 1 - MAÑANA"], "2026-07-14", "PENDIENTE"),
    (usr_map["jpalma"], cur_map["CE102"], esp_map["Aula 102"], bloq_map["BLOQUE 7 - NOCHE"], "2026-07-15", "CANCELADA"),
]
for r in reservas_data:
    cur.execute(
        "INSERT INTO reservas (id_usuario, id_curso, id_espacio, id_bloque, fecha, estado) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        r
    )

# --- 11. PROCESAMIENTO_NLP ---
print("Insertando procesamiento_nlp...")
nlp_data = [
    (usr_map["obaylon"], "Quiero reservar el laboratorio de computo para el lunes", "RESERVAR_ESPACIO", '{"intencion": "reserva", "entidad": "laboratorio"}', '{"accion": "buscar_espacio", "params": {}}', "gpt-4o-mini", 450),
    (usr_map["obaylon"], "¿Que cursos tengo esta semana?", "CONSULTAR_HORARIO", '{"intencion": "horario", "periodo": "semanal"}', '{"accion": "listar_cursos", "params": {}}', "gpt-4o-mini", 320),
    (usr_map["jpalma"], "Muestra las reservas del aula 101", "CONSULTAR_RESERVAS", '{"intencion": "reservas", "espacio": "Aula 101"}', '{"accion": "listar_reservas", "params": {"espacio": "Aula 101"}}', "gpt-4o-mini", 510),
]
for n in nlp_data:
    cur.execute(
        "INSERT INTO procesamiento_nlp (id_usuario, prompt_original, intencion_detectada, entidades_encontradas, resultado_json, modelo_usado, tiempo_procesamiento_ms) VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
        n
    )

conn.commit()
cur.close()
conn.close()
print("\nSeed completado exitosamente!")
