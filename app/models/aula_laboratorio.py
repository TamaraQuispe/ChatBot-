from .espacio import EspacioAcademico
from config.database import Database


class AulaLaboratorio(EspacioAcademico):
    def __init__(self, db: Database):
        super().__init__(db)
        self.tipo_fijo = "LABORATORIO"

    def verificar_software(self, id_espacio: int, requerido: str) -> bool:
        conn = self.db.obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT software FROM espacios_academicos WHERE id_espacio = %s",
            (id_espacio,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return requerido.lower() in row["software"].lower()
        return False
