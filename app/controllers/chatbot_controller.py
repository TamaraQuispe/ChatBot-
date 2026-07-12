"""Adapter: ChatbotController legacy → nueva arquitectura."""

from typing import Optional
from config.database import Database
from app.services.chat_service import ChatService
from app.logger import get_logger

logger = get_logger("chatbot")


class ChatbotController:
    def __init__(self, db: Database = None):
        self.chat_service = ChatService()

    def procesar_query(self, id_usuario: int, mensaje: str,
                       historial: list) -> dict:
        try:
            resultado = self.chat_service.procesar_mensaje(
                id_usuario, mensaje, historial=historial
            )
            logger.info(
                f"Query procesada: usuario={id_usuario}, "
                f"accion={resultado.get('tipo')}"
            )
            return resultado
        except Exception as e:
            logger.error(f"Error procesando query: {e}")
            return {
                "tipo": "bot",
                "texto": "Ocurrió un error al procesar tu consulta.",
            }
