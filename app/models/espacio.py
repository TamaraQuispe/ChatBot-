from typing import Optional
from config.database import Database
from core.logger import get_logger

logger = get_logger("espacio")


ESTADOS_ESPACIO = {1: "DISPONIBLE", 2: "OCUPADO", 3: "MANTENIMIENTO"}
ESTADOS_ESPACIO_REV = {"DISPONIBLE": 1, "OCUPADO": 2, "MANTENIMIENTO": 3}


class EspacioAcademico:
    def __init__(self, db: Database):
        self.db = db

    def buscar_disponibles(self, tipo: str) -> list:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM espacios_academicos WHERE tipo = %s AND estado = 1",
                (tipo,)
            )
            filas = cursor.fetchall()
            conn.close()
            return [dict(f) for f in filas]
        except Exception as e:
            logger.error(f"Error buscando disponibles: {e}")
            return []

    def listar_todos(self) -> list:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM espacios_academicos ORDER BY id_espacio"
            )
            filas = cursor.fetchall()
            conn.close()
            for f in filas:
                estado_num = f.get("estado")
                if estado_num in ESTADOS_ESPACIO:
                    f["estado_texto"] = ESTADOS_ESPACIO[estado_num]
                else:
                    f["estado_texto"] = "DESCONOCIDO"
            return [dict(f) for f in filas]
        except Exception as e:
            logger.error(f"Error listando espacios: {e}")
            return []

    def ocupar(self, id_espacio: int) -> bool:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE espacios_academicos SET estado = 2 WHERE id_espacio = %s",
                (id_espacio,)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            logger.error(f"Error ocupando espacio: {e}")
            return False

    def liberar(self, id_espacio: int) -> bool:
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE espacios_academicos SET estado = 1 WHERE id_espacio = %s",
                (id_espacio,)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            logger.error(f"Error liberando espacio: {e}")
            return False

    @staticmethod
    def crear_tabla(db: Database):
        try:
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
                    estado SMALLINT NOT NULL DEFAULT 1,
                    fecha_creacion TIMESTAMP DEFAULT NOW()
                );
            """)
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Error creando tabla espacios_academicos: {e}")

    @staticmethod
    def sembrar(db: Database):
        try:
            conn = db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) AS count FROM espacios_academicos;")
            if cursor.fetchone()["count"] > 0:
                conn.close()
                return
            espacios = [
                ("Aula de Computo 402", "COMPUTO", "Torre B - Piso 4", 40, "i7 Gen 12 + GPU, Internet", "VS Code, IntelliJ", 1),
                ("Aula Teorica 204", "TEORICA", "Torre A - Piso 2", 50, "Proyector + Pizarra", "Ninguno", 1),
                ("Laboratorio Quimica 101", "LABORATORIO", "Torre C - Piso 1", 30, "Microscopios, Bunsen", "Simulador Lab", 1),
                ("Sala de Computo 301", "COMPUTO", "Torre B - Piso 3", 35, "i5 Gen 13, Red", "Python, RStudio", 1),
            ]
            for e in espacios:
                cursor.execute(
                    "INSERT INTO espacios_academicos (nombre, tipo, ubicacion, capacidad, equipamiento, software, estado) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    e
                )
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Error sembrando espacios: {e}")
