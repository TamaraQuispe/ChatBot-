"""Adapter: Chatbot model legacy → nueva arquitectura."""

from typing import Optional
from app.services.chat_service import ChatService
from app.logger import get_logger

logger = get_logger("chatbot")


class Chatbot:
    def __init__(self, db=None):
        self.chat_service = ChatService()

    def procesar_mensaje(self, id_usuario: int, mensaje: str,
                         historial: list) -> dict:
        return self.chat_service.procesar_mensaje(id_usuario, mensaje)

    @staticmethod
    def crear_tabla(db=None):
        pass
