"""Adapter: AuthController legacy → nueva arquitectura."""

from app.services.auth_service import AuthService
from app.logger import get_logger
from app.utils import escapar

logger = get_logger("auth")


class AuthController:
    def __init__(self, db=None):
        self.auth_service = AuthService()

    def login(self, username: str, password: str) -> dict:
        try:
            if not username or not password:
                logger.warning("Intento de login con campos vacíos")
                return None
            username = escapar(username.strip())
            if len(username) > 100 or len(password) > 255:
                logger.warning("Login con longitud excedida")
                return None
            return self.auth_service.login(username, password)
        except Exception as e:
            logger.error(f"Error en login: {e}")
            return None
