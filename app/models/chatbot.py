from typing import Optional
from config.database import Database
from .procesador_nlp import ProcesadorNLP
from .gestor_reservas import GestorReservas
from app.controllers.reserva_controller import ReservaController
from app.services.ollama_service import OllamaService
from core.logger import get_logger

logger = get_logger("chatbot")


class Chatbot:
    def __init__(self, db: Database):
        self.db = db
        self.nlp = ProcesadorNLP(db)
        self.reserva_ctrl = ReservaController(db)
        self.gestor = GestorReservas(db)
        self.ollama = OllamaService()

    def procesar_mensaje(self, id_usuario: int, mensaje: str, historial: list) -> dict:
        resultado = self.nlp.procesar(id_usuario, mensaje)
        accion = resultado.get("accion", "consulta")
        if accion == "reservar":
            aulas = self.reserva_ctrl.buscar_disponibilidad(mensaje)
            if aulas:
                return {"tipo": "card", "data": aulas[0]}
            else:
                contexto = "No hay disponibilidad actual"
                respuesta = self.ollama.consultar(mensaje, contexto)
                return {"tipo": "bot", "texto": respuesta}
        elif accion == "listar":
            reservas = self.gestor.reservas_por_usuario(id_usuario)
            if reservas:
                texto = "Tus reservas activas:\n" + "\n".join(
                    [f"- {r['espacio_nombre']} ({r['fecha']} {r['horario']})" for r in reservas]
                )
            else:
                texto = "No tienes reservas activas."
            return {"tipo": "bot", "texto": texto}
        else:
            aulas = self.reserva_ctrl.buscar_disponibilidad(mensaje)
            contexto = f"Salones disponibles: {aulas}" if aulas else "No hay disponibilidad"
            respuesta = self.ollama.consultar(mensaje, contexto)
            return {"tipo": "bot", "texto": respuesta}
