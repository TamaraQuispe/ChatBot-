import os
import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    def __init__(self, database_url=None):
        self.database_url = database_url or os.environ.get("DATABASE_URL")
        if not self.database_url:
            raise ValueError(
                "Define DATABASE_URL en .env o como variable de entorno. "
                "Ej: DATABASE_URL=postgresql://user:pass@host:5432/dbname"
            )

    def obtener_conexion(self):
        try:
            conn = psycopg2.connect(self.database_url)
            conn.cursor_factory = RealDictCursor
            return conn
        except psycopg2.Error as e:
            print(f"Error de conexion PostgreSQL: {e}")
            raise e
