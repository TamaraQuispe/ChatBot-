"""Tests para DTOs."""

import pytest
from app.dto.user_dto import UserDTO, LoginResponseDTO, UserListDTO
from app.dto.espacio_dto import EspacioDTO, EspacioListDTO, TipoEspacioDTO
from app.dto.reserva_dto import ReservaDTO, ReservaListDTO
from app.dto.chat_dto import MensajeDTO, HistorialDTO
from app.dto.admin_dto import EstadisticasDTO


class TestUserDTO:
    def test_from_dict(self):
        data = {"id_usuario": 1, "username": "docente1", "nombre": "Carlos", "rol": "DOCENTE"}
        dto = UserDTO.from_dict(data)
        assert dto.id_usuario == 1
        assert dto.username == "docente1"
        assert dto.rol == "DOCENTE"

    def test_to_dict(self):
        dto = UserDTO(id_usuario=1, username="admin", nombre="Admin", rol="ADMIN", correo="a@b.com")
        d = dto.to_dict()
        assert d["username"] == "admin"
        assert d["correo"] == "a@b.com"

    def test_default_correo(self):
        dto = UserDTO(id_usuario=1, username="u", nombre="U", rol="DOCENTE")
        assert dto.correo == ""


class TestLoginResponseDTO:
    def test_to_dict(self):
        user = UserDTO(id_usuario=1, username="u", nombre="U", rol="DOCENTE")
        resp = LoginResponseDTO(usuario=user, token="abc123")
        d = resp.to_dict()
        assert d["token"] == "abc123"
        assert d["usuario"]["username"] == "u"


class TestEspacioDTO:
    def test_from_dict(self):
        data = {"id_espacio": 1, "nombre": "Lab 101", "tipo": "LABORATORIO", "ubicacion": "A", "capacidad": 30, "estado": "DISPONIBLE"}
        dto = EspacioDTO.from_dict(data)
        assert dto.id_espacio == 1
        assert dto.tipo == "LABORATORIO"

    def test_to_dict_removes_tipo_nombre(self):
        dto = EspacioDTO(id_espacio=1, nombre="Lab", tipo="AULA", ubicacion="X", capacidad=20, estado="DISP", tipo_nombre="AULA")
        d = dto.to_dict()
        assert "tipo_nombre" not in d
        assert d["tipo"] == "AULA"


class TestReservaDTO:
    def test_from_dict(self):
        data = {"id_reserva": 1, "id_usuario": 1, "id_espacio": 1, "curso_nombre": "Mat", "horario": "08:00", "fecha": "2026-01-01", "estado": "CONFIRMADA"}
        dto = ReservaDTO.from_dict(data)
        assert dto.estado == "CONFIRMADA"


class TestMensajeDTO:
    def test_to_dict(self):
        dto = MensajeDTO(mensaje="Hola", respuesta="¿En qué puedo ayudarte?")
        d = dto.to_dict()
        assert d["mensaje"] == "Hola"
        assert d["tipo"] == "chat"


class TestEstadisticasDTO:
    def test_defaults(self):
        dto = EstadisticasDTO()
        d = dto.to_dict()
        assert d["total_usuarios"] == 0
        assert d["por_tipo"] == {}

    def test_custom_values(self):
        dto = EstadisticasDTO(total_usuarios=10, total_espacios=5, por_tipo={"AULA": 3})
        d = dto.to_dict()
        assert d["total_usuarios"] == 10
        assert d["por_tipo"]["AULA"] == 3
