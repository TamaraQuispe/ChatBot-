"""DTO para respuestas de administración."""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class EstadisticasDTO:
    total_usuarios: int = 0
    total_espacios: int = 0
    reservas_activas: int = 0
    espacios_disponibles: int = 0
    ocupados: int = 0
    por_tipo: dict = None
    total_reservas: int = 0
    reservas_pendientes: int = 0
    tasa_ocupacion: float = 0.0

    def __post_init__(self):
        if self.por_tipo is None:
            self.por_tipo = {}

    def to_dict(self) -> dict:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class BloqueHorarioDTO:
    id_bloque: int
    dia_semana: str
    hora_inicio: str
    hora_fin: str
    id_espacio: int | None = None
    espacio_nombre: str = ""
    tipo: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class FacultadDTO:
    nombre: str
    total_espacios: int = 0
    reservas: int = 0
    disponibles: int = 0

    def to_dict(self) -> dict:
        return asdict(self)
