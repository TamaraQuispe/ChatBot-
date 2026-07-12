"""Repositorio base con operaciones CRUD genéricas."""

from typing import Optional, Any
from app.database.connection import fetch_one, fetch_all, execute, execute_returning


class BaseRepository:
    """Repositorio genérico con métodos CRUD básicos."""

    table: str = ""
    pk: str = "id"

    def get_by_id(self, id_val: Any) -> Optional[dict]:
        return fetch_one(
            f"SELECT * FROM {self.table} WHERE {self.pk} = %s", (id_val,)
        )

    def get_all(self, order_by: str = "") -> list:
        order = f"ORDER BY {order_by}" if order_by else ""
        return fetch_all(f"SELECT * FROM {self.table} {order}")

    def delete(self, id_val: Any) -> bool:
        affected = execute(
            f"DELETE FROM {self.table} WHERE {self.pk} = %s", (id_val,)
        )
        return affected > 0

    def count(self, where_clause: str = "", params: tuple = ()) -> int:
        where = f"WHERE {where_clause}" if where_clause else ""
        row = fetch_one(
            f"SELECT COUNT(*) as count FROM {self.table} {where}", params
        )
        return row["count"] if row else 0
