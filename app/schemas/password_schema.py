"""Schemas de validación para restablecimiento de contraseña."""
import re
from dataclasses import dataclass


_PASSWORD_REGEX = re.compile(
    r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>_\-]).{8,}$"
)


@dataclass
class ForceChangePasswordSchema:
    new_password: str
    confirm_password: str

    @classmethod
    def from_dict(cls, data: dict) -> "ForceChangePasswordSchema":
        return cls(
            new_password=data.get("new_password", ""),
            confirm_password=data.get("confirm_password", ""),
        )

    def validate(self) -> list[str]:
        errors = []
        if not self.new_password:
            errors.append("La nueva contraseña es obligatoria")
        elif not _PASSWORD_REGEX.match(self.new_password):
            errors.append(
                "La contraseña debe tener al menos 8 caracteres, "
                "una mayúscula, una minúscula, un número y un carácter especial"
            )
        if not self.confirm_password:
            errors.append("La confirmación de contraseña es obligatoria")
        elif self.new_password != self.confirm_password:
            errors.append("Las contraseñas no coinciden")
        return errors
