"""DTO para respuestas del chatbot."""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class MensajeDTO:
    mensaje: str
    respuesta: str
    tipo: str = "chat"

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class HistorialDTO:
    mensajes: list[dict]

    def to_dict(self) -> dict:
        return {"mensajes": self.mensajes, "total": len(self.mensajes)}
