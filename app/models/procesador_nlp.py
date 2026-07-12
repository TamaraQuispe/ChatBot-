"""Adapter: ProcesadorNLP legacy → nueva arquitectura."""

from app.services.nlp_service import NLPService
from app.logger import get_logger

logger = get_logger("nlp")


class ProcesadorNLP:
    def __init__(self, db=None):
        self.service = NLPService()

    def procesar(self, id_usuario: int, prompt: str) -> dict:
        return self.service.procesar(id_usuario, prompt)
