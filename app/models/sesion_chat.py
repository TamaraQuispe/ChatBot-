"""Adapter: SesionChat model legacy → nueva arquitectura."""

from typing import Optional
from app.repositories.chat_repository import SesionChatRepository, MensajeChatRepository
from app.logger import get_logger

logger = get_logger("sesion_chat")


class SesionChat:
    def __init__(self, db=None):
        self.repo = SesionChatRepository()
        self.msg_repo = MensajeChatRepository()

    def crear(self, id_usuario: int) -> Optional[dict]:
        return self.repo.create(id_usuario)

    def listar_por_usuario(self, id_usuario: int) -> list:
        return self.repo.get_by_usuario(id_usuario)

    def obtener_mensajes(self, id_sesion: int) -> list:
        return self.msg_repo.get_by_sesion(id_sesion)

    def guardar_mensaje(self, id_sesion: int, tipo: str, contenido: str):
        self.msg_repo.create(id_sesion, tipo, contenido)
