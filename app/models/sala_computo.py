from .aula_laboratorio import AulaLaboratorio
from config.database import Database


class SalaComputo(AulaLaboratorio):
    def __init__(self, db: Database):
        super().__init__(db)
        self.tipo_fijo = "COMPUTO"

    def tiene_conexion_internet(self, id_espacio: int) -> bool:
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT equipamiento FROM espacios_academicos WHERE id_espacio = %s",
            (id_espacio,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return "internet" in row["equipamiento"].lower() or "red" in row["equipamiento"].lower()
        return False
