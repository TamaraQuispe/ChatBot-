"""Tests para servicios con mocking de repositorios."""

import pytest
from unittest.mock import patch, MagicMock
from app.services.auth_service import AuthService
from app.services.reserva_service import ReservaService
from app.exceptions import ValidationError, UnauthorizedError


@patch("app.services.auth_service.UsuarioRepository")
class TestAuthService:
    def test_login_exitoso(self, mock_repo_class):
        mock_repo = MagicMock()
        mock_repo_class.return_value = mock_repo
        mock_repo.get_by_username.return_value = {
            "id_usuario": 1, "username": "docente1", "password_hash": "$2b$12$hash",
            "nombre": "Carlos", "correo": "c@utp.edu.pe", "rol": "DOCENTE",
        }
        with patch("bcrypt.checkpw", return_value=True):
            service = AuthService()
            result = service.login("docente1", "secreta123")
            assert result is not None
            assert result["username"] == "docente1"
            assert result["rol"] == "DOCENTE"

    def test_login_usuario_vacio(self, mock_repo_class):
        service = AuthService()
        with pytest.raises(ValidationError):
            service.login("", "")

    def test_login_usuario_no_encontrado(self, mock_repo_class):
        mock_repo = MagicMock()
        mock_repo_class.return_value = mock_repo
        mock_repo.get_by_username.return_value = None
        service = AuthService()
        with pytest.raises(UnauthorizedError):
            service.login("noexiste", "pass")


@patch("app.services.reserva_service.ReservaRepository")
@patch("app.services.reserva_service.EspacioRepository")
class TestReservaService:
    def test_crear_exitoso(self, mock_espacio_repo_class, mock_repo_class):
        mock_repo = MagicMock()
        mock_espacio_repo = MagicMock()
        mock_repo_class.return_value = mock_repo
        mock_espacio_repo_class.return_value = mock_espacio_repo
        mock_espacio_repo.get_by_id.return_value = {"id_espacio": 1, "estado": "DISPONIBLE"}
        mock_repo.create.return_value = {"id_reserva": 1, "id_espacio": 1, "id_usuario": 1, "estado": "PENDIENTE"}

        with patch("app.database.connection.execute"):
            service = ReservaService()
            result = service.crear(id_usuario=1, id_espacio=1, curso_nombre="Matemáticas", horario="08:00-10:00")
            assert result is not None
            assert result["id_reserva"] == 1

    def test_crear_id_usuario_invalido(self, mock_espacio_repo_class, mock_repo_class):
        service = ReservaService()
        with pytest.raises(ValidationError):
            service.crear(id_usuario=-1, id_espacio=1)
