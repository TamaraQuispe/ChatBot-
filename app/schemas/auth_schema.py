"""Schemas de autenticación."""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class LoginSchema:
    username: str
    password: str

    def validate(self) -> list[str]:
        errors = []
        if not self.username or not self.username.strip():
            errors.append("El nombre de usuario es requerido")
        elif len(self.username) > 100:
            errors.append("El nombre de usuario no debe exceder 100 caracteres")
        if not self.password:
            errors.append("La contraseña es requerida")
        elif len(self.password) > 255:
            errors.append("La contraseña no debe exceder 255 caracteres")
        return errors

    @classmethod
    def from_dict(cls, data: dict) -> "LoginSchema":
        return cls(
            username=data.get("username", "").strip(),
            password=data.get("password", ""),
        )


@dataclass
class RegisterSchema:
    username: str
    password: str
    nombre: str
    correo: str
    rol: str = "DOCENTE"

    def validate(self) -> list[str]:
        errors = []
        import re
        if not self.username or not self.username.strip():
            errors.append("El nombre de usuario es requerido")
        elif not re.match(r"^[a-zA-Z0-9_]{3,50}$", self.username):
            errors.append("El usuario debe tener entre 3 y 50 caracteres alfanuméricos")
        if not self.password:
            errors.append("La contraseña es requerida")
        elif len(self.password) < 6:
            errors.append("La contraseña debe tener al menos 6 caracteres")
        elif len(self.password) > 128:
            errors.append("La contraseña no debe exceder 128 caracteres")
        if not self.nombre or not self.nombre.strip():
            errors.append("El nombre es requerido")
        elif len(self.nombre) > 100:
            errors.append("El nombre no debe exceder 100 caracteres")
        if not self.correo or not self.correo.strip():
            errors.append("El correo es requerido")
        elif not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", self.correo):
            errors.append("El correo no tiene un formato válido")
        if self.rol and self.rol not in ("DOCENTE", "ADMIN"):
            errors.append("El rol debe ser DOCENTE o ADMIN")
        return errors

    @classmethod
    def from_dict(cls, data: dict) -> "RegisterSchema":
        return cls(
            username=data.get("username", "").strip(),
            password=data.get("password", ""),
            nombre=data.get("nombre", "").strip(),
            correo=data.get("correo", "").strip(),
            rol=data.get("rol", "DOCENTE").upper(),
        )
