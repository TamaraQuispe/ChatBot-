from config.database import Database


class EspacioAcademico:
    def __init__(self, db: Database):
        self.db = db

    def buscar_disponibles(self, tipo: str):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM espacios_academicos WHERE tipo = %s AND estado = 'DISPONIBLE'",
            (tipo,)
        )
        filas = cursor.fetchall()
        conn.close()
        return [dict(f) for f in filas]

    def listar_todos(self):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM espacios_academicos ORDER BY id_espacio")
        filas = cursor.fetchall()
        conn.close()
        return [dict(f) for f in filas]

    def ocupar(self, id_espacio: int):
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE espacios_academicos SET estado = 'OCUPADO' WHERE id_espacio = %s",
            (id_espacio,)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def crear_tabla(db: Database):
        conn = db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS espacios_academicos (
                id_espacio SERIAL PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                tipo VARCHAR(100) NOT NULL,
                ubicacion VARCHAR(255) NOT NULL,
                capacidad INTEGER NOT NULL,
                equipamiento TEXT NOT NULL,
                software TEXT NOT NULL,
                estado VARCHAR(50) NOT NULL DEFAULT 'DISPONIBLE',
                fecha_creacion TIMESTAMP DEFAULT NOW()
            );
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def sembrar(db: Database):
        conn = db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) AS count FROM espacios_academicos;")
        if cursor.fetchone()["count"] > 0:
            conn.close()
            return
        espacios = [
            ("Aula de Computo 402", "COMPUTO", "Torre B - Piso 4", 40, "i7 Gen 12 + GPU", "VS Code, IntelliJ", "DISPONIBLE"),
            ("Aula Teorica 204", "TEORICA", "Torre A - Piso 2", 50, "Proyector + Pizarra", "Ninguno", "DISPONIBLE"),
        ]
        for e in espacios:
            cursor.execute(
                "INSERT INTO espacios_academicos (nombre, tipo, ubicacion, capacidad, equipamiento, software, estado) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                e
            )
        conn.commit()
        conn.close()
