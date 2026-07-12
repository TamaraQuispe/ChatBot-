"""Servicio de chatbot - orquestación NLP + OpenRouter + memoria."""

import json
from app.repositories.chat_repository import SesionChatRepository, MensajeChatRepository
from app.services.openrouter_service import OpenRouterService
from app.services.reserva_service import ReservaService
from app.services.nlp_service import NLPService
from app.logger import get_logger

logger = get_logger("chat_service")


class ChatService:
    def __init__(self):
        self.sesion_repo = SesionChatRepository()
        self.mensaje_repo = MensajeChatRepository()
        self.reserva_repo = ReservaRepository()
        self.nlp = NLPService()
        self.reserva_service = ReservaService()
        try:
            self.ors = OpenRouterService()
        except Exception:
            self.ors = None
            logger.warning("OpenRouter no disponible")

    def procesar_mensaje(self, id_usuario: int, mensaje: str,
                         id_sesion: int | None = None,
                         historial: list | None = None) -> dict:
        resultado_nlp = self.nlp.procesar(id_usuario, mensaje)
        accion = resultado_nlp.get("accion", "consulta")

        self.mensaje_repo.create(id_sesion or 0, "user", json.dumps({"texto": mensaje}))

        if accion == "reservar":
            return self._procesar_reserva(id_usuario, mensaje)
        elif accion == "listar":
            return self._listar_reservas(id_usuario)
        elif accion == "cancelar":
            return self._cancelar_reserva(id_usuario, mensaje)
        else:
            return self._consulta_general(id_usuario, mensaje)

    def _procesar_reserva(self, id_usuario: int, mensaje: str) -> dict:
        aulas = self.reserva_service.buscar_disponibilidad(mensaje)
        if aulas:
            respuesta = {"tipo": "card", "data": aulas[0]}
        else:
            try:
                if self.ors:
                    texto = self.ors.consultar(mensaje, "No hay disponibilidad actual")
                else:
                    texto = "No hay disponibilidad actual."
            except Exception:
                texto = "Lo siento, el servicio de IA no está disponible."
            respuesta = {"tipo": "bot", "texto": texto}
        return respuesta

    def _listar_reservas(self, id_usuario: int) -> dict:
        reservas = self.reserva_repo.get_by_usuario(id_usuario)
        if reservas:
            texto = "Tus reservas activas:\n" + "\n".join(
                f"- {r['espacio_nombre']} ({r['fecha']} {r.get('horario', '')})"
                for r in reservas
            )
        else:
            texto = "No tienes reservas activas."
        return {"tipo": "bot", "texto": texto}

    def _cancelar_reserva(self, id_usuario: int, mensaje: str) -> dict:
        texto = "Para cancelar una reserva, ve a Mis Reservas y usa la opción Cancelar."
        return {"tipo": "bot", "texto": texto}

    def _consulta_general(self, id_usuario: int, mensaje: str) -> dict:
        aulas = self.reserva_service.buscar_disponibilidad(mensaje)
        contexto = f"Salones disponibles: {aulas}" if aulas else "No hay disponibilidad"
        try:
            if self.ors:
                respuesta = self.ors.consultar(mensaje, contexto)
            else:
                respuesta = "Lo siento, el servicio de IA no está disponible."
        except Exception:
            respuesta = "Lo siento, el servicio de IA no está disponible."
        return {"tipo": "bot", "texto": respuesta}

    def crear_sesion(self, id_usuario: int, titulo: str = "Nuevo Chat") -> dict:
        return self.sesion_repo.create(id_usuario, titulo)

    def listar_sesiones(self, id_usuario: int) -> list:
        return self.sesion_repo.get_by_usuario(id_usuario)

    def obtener_historial(self, id_sesion: int) -> list:
        return self.mensaje_repo.get_by_sesion(id_sesion)
