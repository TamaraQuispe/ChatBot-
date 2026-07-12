"""Schemas de reservas."""

from dataclasses import dataclass


@dataclass
class CrearReservaSchema:
    id_espacio: int
    curso_nombre: str
    horario: str
    fecha: str
    id_usuario: int = 0

    def validate(self) -> list[str]:
        errors = []
        if not isinstance(self.id_espacio, int) or self.id_espacio <= 0:
            errors.append("El ID del espacio debe ser un número positivo")
        if not self.curso_nombre or not self.curso_nombre.strip():
            errors.append("El nombre del curso es requerido")
        elif len(self.curso_nombre) > 200:
            errors.append("El nombre del curso no debe exceder 200 caracteres")
        if not self.horario or not self.horario.strip():
            errors.append("El horario es requerido")
        elif len(self.horario) > 50:
            errors.append("El horario no debe exceder 50 caracteres")
        if not self.fecha or not self.fecha.strip():
            errors.append("La fecha es requerida")
        return errors

    @classmethod
    def from_dict(cls, data: dict) -> "CrearReservaSchema":
        try:
            id_espacio = int(data.get("id_espacio", 0))
        except (ValueError, TypeError):
            id_espacio = 0
        try:
            id_usuario = int(data.get("id_usuario", 0))
        except (ValueError, TypeError):
            id_usuario = 0
        return cls(
            id_espacio=id_espacio,
            curso_nombre=data.get("curso_nombre", "").strip(),
            horario=data.get("horario", "").strip(),
            fecha=data.get("fecha", "").strip(),
            id_usuario=id_usuario,
        )


@dataclass
class CancelarReservaSchema:
    id_reserva: int

    def validate(self) -> list[str]:
        errors = []
        if not isinstance(self.id_reserva, int) or self.id_reserva <= 0:
            errors.append("El ID de la reserva debe ser un número positivo")
        return errors

    @classmethod
    def from_dict(cls, data: dict) -> "CancelarReservaSchema":
        try:
            id_reserva = int(data.get("id_reserva", 0))
        except (ValueError, TypeError):
            id_reserva = 0
        return cls(id_reserva=id_reserva)
