"""Servicio de autenticación - login, registro, gestión de sesiones."""

import bcrypt
from typing import Optional
from app.repositories.usuario_repository import UsuarioRepository
from app.logger import get_logger
from app.exceptions import UnauthorizedError, ValidationError, NotFoundError

logger = get_logger("auth_service")


class AuthService:
    def __init__(self):
        self.usuario_repo = UsuarioRepository()

    def login(self, username: str, password: str) -> Optional[dict]:
        if not username or not password:
            raise ValidationError("Usuario y contraseña son requeridos")

        if len(username) > 100 or len(password) > 255:
            raise ValidationError("Credenciales inválidas")

        username = username.strip()
        usuario = self.usuario_repo.get_by_username(username)

        if not usuario:
            logger.info(f"Intento de login: usuario no encontrado: {username}")
            raise UnauthorizedError("Credenciales inválidas")

        password_hash = usuario.get("password_hash") or usuario.get("password")
        if not password_hash:
            logger.error(f"Usuario {username} no tiene password_hash")
            raise UnauthorizedError("Error de configuración de cuenta")

        if not bcrypt.checkpw(
            password.encode("utf-8"),
            password_hash.encode("utf-8"),
        ):
            logger.info(f"Intento de login: contraseña incorrecta para: {username}")
            raise UnauthorizedError("Credenciales inválidas")

        rol = self._determinar_rol(usuario)
        logger.info(f"Login exitoso: {username} ({rol})")

        return {
            "id_usuario": usuario["id_usuario"],
            "username": usuario["username"],
            "rol": rol,
            "nombre": usuario["nombre"],
            "correo": usuario.get("correo", ""),
        }

    def register(self, data: dict) -> dict:
        existing = self.usuario_repo.get_by_username(data["username"])
        if existing:
            raise ValidationError("El nombre de usuario ya existe")

        existing_email = self.usuario_repo.get_by_correo(data["correo"])
        if existing_email:
            raise ValidationError("El correo ya está registrado")

        hashed = bcrypt.hashpw(
            data["password"].encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

        usuario = self.usuario_repo.create({
            "username": data["username"],
            "password": hashed,
            "nombre": data["nombre"],
            "correo": data["correo"],
            "rol": data.get("rol", "DOCENTE"),
        })

        logger.info(f"Usuario registrado: {data['username']}")
        return usuario

    def _determinar_rol(self, usuario: dict) -> str:
        if usuario.get("rol"):
            return usuario["rol"]
        return "Docente"
