from typing import Optional
from config.database import Database
from app.models.chatbot import Chatbot
from app.models.procesador_nlp import ProcesadorNLP
from core.logger import get_logger

logger = get_logger("chatbot")


class ChatbotController:
    def __init__(self, db: Database):
        self.db = db
        self.chatbot = Chatbot(db)
        self.nlp = ProcesadorNLP(db)

    def procesar_query(self, id_usuario: int, mensaje: str, historial: list) -> dict:
        try:
            resultado = self.chatbot.procesar_mensaje(id_usuario, mensaje, historial)
            logger.info(f"Query procesada: usuario={id_usuario}, accion={resultado.get('tipo')}")
            return resultado
        except Exception as e:
            logger.error(f"Error procesando query: {e}")
            return {"tipo": "bot", "texto": "Ocurrio un error al procesar tu consulta."}
