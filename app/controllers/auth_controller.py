from app.models.usuario import Usuario
from core.logger import get_logger
from core.utils import escapar

logger = get_logger("auth")


class AuthController:
    def __init__(self, db):
        self.usuario_model = Usuario(db)

    def login(self, username: str, password: str):
        try:
            if not username or not password:
                logger.warning("Intento de login con campos vacios")
                return None
            username = escapar(username.strip())
            if len(username) > 100 or len(password) > 255:
                logger.warning("Login con longitud excedida")
                return None
            usuario = self.usuario_model.login(username, password)
            if not usuario:
                logger.info(f"Login fallido para usuario: {username}")
            return usuario
        except Exception as e:
            logger.error(f"Error en login: {str(e)}")
            return None
