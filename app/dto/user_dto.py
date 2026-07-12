"""DTO para respuestas de autenticación y usuarios."""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class UserDTO:
    id_usuario: int
    username: str
    nombre: str
    rol: str
    correo: str = ""
    estado: str = "ACTIVO"

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "UserDTO":
        return cls(
            id_usuario=data.get("id_usuario", 0),
            username=data.get("username", ""),
            nombre=data.get("nombre", ""),
            rol=data.get("rol", "DOCENTE"),
            correo=data.get("correo", ""),
            estado=data.get("estado", "ACTIVO"),
        )


@dataclass
class LoginResponseDTO:
    usuario: UserDTO
    token: str = ""

    def to_dict(self) -> dict:
        return {"usuario": self.usuario.to_dict(), "token": self.token}


@dataclass
class UserListDTO:
    usuarios: list[UserDTO]
    total: int = 0

    def to_dict(self) -> dict:
        return {
            "usuarios": [u.to_dict() for u in self.usuarios],
            "total": self.total or len(self.usuarios),
        }
