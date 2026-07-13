"""Servicio de restablecimiento de contraseña por administrador."""
import secrets
import string
import bcrypt
from typing import Optional
from app.repositories.usuario_repository import UsuarioRepository
from app.logger import get_logger
from app.exceptions import NotFoundError, ValidationError, UnauthorizedError

logger = get_logger("password_reset_service")


class PasswordResetService:
    def __init__(self):
        self.usuario_repo = UsuarioRepository()

    def generar_temp_password(self, length: int = 10) -> str:
        mayus = string.ascii_uppercase
        minus = string.ascii_lowercase
        digitos = string.digits
        all_chars = mayus + minus + digitos
        password = [
            secrets.choice(mayus),
            secrets.choice(minus),
            secrets.choice(digitos),
        ]
        password += [secrets.choice(all_chars) for _ in range(length - 3)]
        secrets.SystemRandom().shuffle(password)
        return "".join(password)

    def reset_password(self, admin_id: int, docente_id: int) -> dict:
        if admin_id == docente_id:
            raise ValidationError("No puedes restablecer tu propia contraseña")
        usuario = self.usuario_repo.get_by_id(docente_id)
        if not usuario:
            raise NotFoundError("Usuario no encontrado")
        temp_password = self.generar_temp_password()
        hashed = bcrypt.hashpw(
            temp_password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
        self.usuario_repo.update_password_with_force(
            docente_id, hashed, force_change=True
        )
        logger.info(
            f"Contraseña restablecida por admin {admin_id} para usuario {docente_id}"
        )
        return {
            "temp_password": temp_password,
            "username": usuario["username"],
            "nombre": usuario["nombre"],
        }

    def force_change_password(
        self, id_usuario: int, current_password: str, new_password: str
    ) -> None:
        usuario = self.usuario_repo.get_by_id(id_usuario)
        if not usuario:
            raise NotFoundError("Usuario no encontrado")
        password_hash = usuario.get("password_hash") or usuario.get("password")
        if not password_hash or not bcrypt.checkpw(
            current_password.encode("utf-8"),
            password_hash.encode("utf-8"),
        ):
            raise ValidationError("La contraseña actual no es correcta")
        hashed = bcrypt.hashpw(
            new_password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
        self.usuario_repo.update_password_with_force(
            id_usuario, hashed, force_change=False
        )
        logger.info(f"Contraseña cambiada forzosamente para usuario {id_usuario}")
