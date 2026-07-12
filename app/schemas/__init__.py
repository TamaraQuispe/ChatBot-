"""Schemas de validación de entrada de datos."""

from app.schemas.auth_schema import LoginSchema, RegisterSchema
from app.schemas.reserva_schema import CrearReservaSchema, CancelarReservaSchema
from app.schemas.chat_schema import MensajeChatSchema
from app.schemas.admin_schema import (
    CrearEspacioSchema,
    CambiarEstadoSchema,
    ActualizarEspacioSchema,
)

__all__ = [
    "LoginSchema",
    "RegisterSchema",
    "CrearReservaSchema",
    "CancelarReservaSchema",
    "MensajeChatSchema",
    "CrearEspacioSchema",
    "CambiarEstadoSchema",
    "ActualizarEspacioSchema",
]
