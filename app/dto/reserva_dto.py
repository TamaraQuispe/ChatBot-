"""DTO para respuestas de reservas."""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class ReservaDTO:
    id_reserva: int
    id_usuario: int
    id_espacio: int
    curso_nombre: str
    horario: str
    fecha: str
    estado: str
    espacio_nombre: str = ""
    usuario_nombre: str = ""
    tipo: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "ReservaDTO":
        return cls(
            id_reserva=data.get("id_reserva", 0),
            id_usuario=data.get("id_usuario", 0),
            id_espacio=data.get("id_espacio", 0),
            curso_nombre=data.get("curso_nombre", ""),
            horario=data.get("horario", ""),
            fecha=data.get("fecha", ""),
            estado=data.get("estado", "PENDIENTE"),
            espacio_nombre=data.get("espacio_nombre", data.get("nombre", "")),
            usuario_nombre=data.get("usuario_nombre", data.get("username", "")),
            tipo=data.get("tipo", ""),
        )


@dataclass
class ReservaListDTO:
    reservas: list[ReservaDTO]
    total: int = 0

    def to_dict(self) -> dict:
        return {
            "reservas": [r.to_dict() for r in self.reservas],
            "total": self.total or len(self.reservas),
        }
