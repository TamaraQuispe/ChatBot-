"""Controlador de restablecimiento de contraseña por administrador."""
from app.services.password_reset_service import PasswordResetService
from app.dto.password_dto import ResetPasswordResponseDTO, ForceChangeResponseDTO
from app.logger import get_logger

logger = get_logger("password_reset_controller")


class PasswordResetController:
    def __init__(self):
        self.service = PasswordResetService()

    def reset_password(self, admin_id: int, docente_id: int) -> dict:
        result = self.service.reset_password(admin_id, docente_id)
        dto = ResetPasswordResponseDTO(
            temp_password=result["temp_password"],
            username=result["username"],
            nombre=result["nombre"],
        )
        return dto.to_dict()

    def force_change_password(
        self, id_usuario: int, current_password: str, new_password: str
    ) -> dict:
        self.service.force_change_password(id_usuario, current_password, new_password)
        return ForceChangeResponseDTO(success=True, message="Contraseña cambiada correctamente").to_dict()
