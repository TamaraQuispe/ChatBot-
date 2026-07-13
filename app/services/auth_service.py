"""Servicio de autenticación - login, registro, gestión de sesiones."""

import bcrypt
from typing import Optional
from app.repositories.usuario_repository import UsuarioRepository
from app.logger import get_logger
from app.exceptions import UnauthorizedError, ValidationError, NotFoundError
from app.schemas.auth_schema import LoginSchema, RegisterSchema

logger = get_logger("auth_service")


class AuthService:
    def __init__(self):
        self.usuario_repo = UsuarioRepository()

    def login(self, username: str, password: str) -> Optional[dict]:
        schema = LoginSchema.from_dict({"username": username, "password": password})
        errors = schema.validate()
        if errors:
            raise ValidationError("; ".join(errors))

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
        schema = RegisterSchema.from_dict(data)
        errors = schema.validate()
        if errors:
            raise ValidationError("; ".join(errors))
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

    def obtener_pregunta(self, username: str) -> Optional[str]:
        usuario = self.usuario_repo.get_by_username(username.strip())
        if not usuario:
            raise NotFoundError("Usuario no encontrado")
        pregunta = usuario.get("pregunta_seguridad") or "¿Cuál es tu código de docente?"
        return pregunta

    def restablecer(self, username: str, respuesta: str, new_password: str) -> bool:
        usuario = self.usuario_repo.get_by_username(username.strip())
        if not usuario:
            raise NotFoundError("Usuario no encontrado")

        respuesta_guardada = (usuario.get("respuesta_seguridad") or "").strip().lower()
        respuesta_dada = respuesta.strip().lower()

        # Si no hay respuesta guardada, usar el username como validación por defecto
        if not respuesta_guardada:
            respuesta_guardada = username.strip().lower()

        if respuesta_dada != respuesta_guardada:
            raise ValidationError("Respuesta de seguridad incorrecta")

        hashed = bcrypt.hashpw(
            new_password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
        self.usuario_repo.update_password(usuario["id_usuario"], hashed)
        logger.info(f"Contraseña restablecida para: {username}")
        return True
