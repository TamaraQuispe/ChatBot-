"""Schemas del chatbot."""

from dataclasses import dataclass


@dataclass
class MensajeChatSchema:
    mensaje: str

    def validate(self) -> list[str]:
        errors = []
        if not self.mensaje or not self.mensaje.strip():
            errors.append("El mensaje no puede estar vacío")
        elif len(self.mensaje) > 2000:
            errors.append("El mensaje no debe exceder 2000 caracteres")
        return errors

    @classmethod
    def from_dict(cls, data: dict) -> "MensajeChatSchema":
        return cls(mensaje=data.get("mensaje", "").strip())
