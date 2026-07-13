"""DTO para restablecimiento de contraseña."""
from dataclasses import dataclass, asdict


@dataclass
class ResetPasswordResponseDTO:
    temp_password: str
    username: str
    nombre: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ForceChangeResponseDTO:
    success: bool
    message: str = ""

    def to_dict(self) -> dict:
        return asdict(self)
