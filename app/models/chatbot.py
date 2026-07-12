from typing import Optional
from config.database import Database
from .procesador_nlp import ProcesadorNLP
from .gestor_reservas import GestorReservas
from app.controllers.reserva_controller import ReservaController
from app.services.openrouter_service import OpenRouterService
from core.logger import get_logger

logger = get_logger("chatbot")


class Chatbot:
    def __init__(self, db: Database):
        self.db = db
        self.nlp = ProcesadorNLP(db)
        self.reserva_ctrl = ReservaController(db)
        self.gestor = GestorReservas(db)
        try:
            self.ors = OpenRouterService()
        except Exception:
            self.ors = None

    def procesar_mensaje(self, id_usuario: int, mensaje: str, historial: list) -> dict:
        resultado = self.nlp.procesar(id_usuario, mensaje)
        accion = resultado.get("accion", "consulta")
        if accion == "reservar":
            aulas = self.reserva_ctrl.buscar_disponibilidad(mensaje)
            if aulas:
                return {"tipo": "card", "data": aulas[0]}
            else:
                try:
                    respuesta = self.ors.consultar(mensaje, "No hay disponibilidad actual")
                except Exception:
                    respuesta = "Lo siento, el servicio de IA no está disponible."
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
            try:
                respuesta = self.ors.consultar(mensaje, contexto)
            except Exception:
                respuesta = "Lo siento, el servicio de IA no está disponible."
            return {"tipo": "bot", "texto": respuesta}
