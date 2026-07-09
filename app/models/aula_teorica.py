from .espacio import EspacioAcademico
from config.database import Database


class AulaTeorica(EspacioAcademico):
    def __init__(self, db: Database):
        super().__init__(db)
        self.tipo_fijo = "TEORICA"

    def tiene_proyector(self, id_espacio: int) -> bool:
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT equipamiento FROM espacios_academicos WHERE id_espacio = %s",
            (id_espacio,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return "proyector" in row["equipamiento"].lower() or "pizarra" in row["equipamiento"].lower()
        return False
