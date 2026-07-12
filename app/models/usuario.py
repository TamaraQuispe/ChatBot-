"""Adapter: Usuario model legacy → nueva arquitectura."""

import bcrypt
from typing import Optional
from app.repositories.usuario_repository import UsuarioRepository
from app.logger import get_logger

logger = get_logger("usuario")


class Usuario:
    def __init__(self, db=None):
        self.repo = UsuarioRepository()

    def login(self, username: str, password_plano: str) -> Optional[dict]:
        try:
            usuario = self.repo.get_by_username(username)
            if not usuario:
                logger.info(f"Usuario no encontrado: {username}")
                return None

            password_hash = usuario.get("password_hash") or usuario.get("password")
            if not password_hash:
                return None

            if not bcrypt.checkpw(
                password_plano.encode("utf-8"),
                password_hash.encode("utf-8"),
            ):
                logger.info(f"Password incorrecto para: {username}")
                return None

            rol = usuario.get("rol", "Docente")
            return {
                "id_usuario": usuario["id_usuario"],
                "username": usuario["username"],
                "rol": rol,
                "nombre": usuario["nombre"],
                "correo": usuario.get("correo", ""),
            }
        except Exception as e:
            logger.error(f"Error en login: {e}", exc_info=True)
            return None

    @staticmethod
    def crear_tabla(db=None):
        pass

    @staticmethod
    def sembrar(db=None):
        pass
