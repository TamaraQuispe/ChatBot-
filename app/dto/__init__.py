"""DTOs - Data Transfer Objects para respuestas estructuradas."""

from app.dto.user_dto import UserDTO, LoginResponseDTO, UserListDTO
from app.dto.espacio_dto import EspacioDTO, EspacioListDTO, TipoEspacioDTO
from app.dto.reserva_dto import ReservaDTO, ReservaListDTO
from app.dto.chat_dto import MensajeDTO, HistorialDTO
from app.dto.admin_dto import EstadisticasDTO, BloqueHorarioDTO, FacultadDTO
from app.dto.password_dto import ResetPasswordResponseDTO, ForceChangeResponseDTO

__all__ = [
    "UserDTO",
    "LoginResponseDTO",
    "UserListDTO",
    "EspacioDTO",
    "EspacioListDTO",
    "TipoEspacioDTO",
    "ReservaDTO",
    "ReservaListDTO",
    "MensajeDTO",
    "HistorialDTO",
    "EstadisticasDTO",
    "BloqueHorarioDTO",
    "FacultadDTO",
    "ResetPasswordResponseDTO",
    "ForceChangeResponseDTO",
]
