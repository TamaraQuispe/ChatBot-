"""DTO para respuestas de espacios académicos."""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class EspacioDTO:
    id_espacio: int
    nombre: str
    tipo: str
    ubicacion: str
    capacidad: int
    estado: str
    equipamiento: str = ""
    software: str = ""
    tipo_nombre: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        if not d.get("tipo") and d.get("tipo_nombre"):
            d["tipo"] = d["tipo_nombre"]
        d.pop("tipo_nombre", None)
        return d

    @classmethod
    def from_dict(cls, data: dict) -> "EspacioDTO":
        return cls(
            id_espacio=data.get("id_espacio", 0),
            nombre=data.get("nombre", ""),
            tipo=data.get("tipo", data.get("tipo_nombre", "")),
            ubicacion=data.get("ubicacion", ""),
            capacidad=data.get("capacidad", 0),
            estado=data.get("estado", "DISPONIBLE"),
            equipamiento=data.get("equipamiento", ""),
            software=data.get("software", ""),
            tipo_nombre=data.get("tipo_nombre", ""),
        )


@dataclass
class EspacioListDTO:
    espacios: list[EspacioDTO]
    total: int = 0

    def to_dict(self) -> dict:
        return {
            "espacios": [e.to_dict() for e in self.espacios],
            "total": self.total or len(self.espacios),
        }


@dataclass
class TipoEspacioDTO:
    id_tipo: int
    nombre: str

    def to_dict(self) -> dict:
        return asdict(self)
