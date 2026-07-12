"""Repositorio de software."""

from typing import Optional
from app.repositories.base import BaseRepository
from app.database.connection import fetch_one, fetch_all


class SoftwareRepository(BaseRepository):
    table = "software"
    pk = "id_software"

    def get_all_with_details(self) -> list:
        return fetch_all("SELECT * FROM software ORDER BY nombre")
