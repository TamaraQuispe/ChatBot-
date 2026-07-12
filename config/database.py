"""Adapter: Configuración de base de datos (legado → nueva arquitectura)."""

# Re-exporta la clase Database original para compatibilidad
# La nueva implementación está en app.database.connection
from app.database.connection import (
    get_connection,
    get_cursor,
    fetch_one,
    fetch_all,
    execute,
    execute_returning,
    init_pool,
    close_pool,
    get_database_url,
)


class Database:
    """Wrapper legacy para mantener compatibilidad con código existente."""

    def __init__(self, database_url=None):
        from app.database.connection import get_database_url
        self.database_url = database_url or get_database_url()

    def obtener_conexion(self):
        conn = get_connection().__enter__()
        # get_connection es un context manager; extraemos la conexión raw
        import psycopg2
        from psycopg2.extras import RealDictCursor
        # Recreamos una conexión directa para compatibilidad
        conn = psycopg2.connect(self.database_url)
        conn.cursor_factory = RealDictCursor
        with conn.cursor() as cur:
            cur.execute("SET search_path TO public")
        return conn
