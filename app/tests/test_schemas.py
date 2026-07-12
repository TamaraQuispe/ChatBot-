"""Tests para Schemas de validación."""

import pytest
from app.schemas.auth_schema import LoginSchema, RegisterSchema
from app.schemas.reserva_schema import CrearReservaSchema, CancelarReservaSchema
from app.schemas.chat_schema import MensajeChatSchema
from app.schemas.admin_schema import CrearEspacioSchema, CambiarEstadoSchema


class TestLoginSchema:
    def test_valido(self):
        s = LoginSchema(username="docente1", password="secreta123")
        assert s.validate() == []

    def test_usuario_vacio(self):
        s = LoginSchema(username="", password="secreta123")
        assert "El nombre de usuario es requerido" in s.validate()

    def test_password_vacio(self):
        s = LoginSchema(username="docente1", password="")
        assert "La contraseña es requerida" in s.validate()

    def test_campos_vacios(self):
        s = LoginSchema(username="", password="")
        errors = s.validate()
        assert len(errors) == 2

    def test_from_dict(self):
        s = LoginSchema.from_dict({"username": "  test  ", "password": "pass"})
        assert s.username == "test"
        assert s.password == "pass"


class TestRegisterSchema:
    def test_valido(self):
        s = RegisterSchema(
            username="nuevo_user",
            password="pass123",
            nombre="Juan Perez",
            correo="juan@utp.edu.pe",
        )
        assert s.validate() == []

    def test_email_invalido(self):
        s = RegisterSchema(
            username="user", password="pass123", nombre="Test", correo="invalido"
        )
        assert "El correo no tiene un formato válido" in s.validate()

    def test_password_corta(self):
        s = RegisterSchema(
            username="user", password="12", nombre="Test", correo="a@b.com"
        )
        assert "La contraseña debe tener al menos 6 caracteres" in s.validate()

    def test_rol_invalido(self):
        s = RegisterSchema(
            username="user", password="123456", nombre="Test", correo="a@b.com", rol="OTRO"
        )
        errors = s.validate()
        assert any("rol" in e.lower() for e in errors)

    def test_username_corto(self):
        s = RegisterSchema(
            username="ab", password="123456", nombre="Test", correo="a@b.com"
        )
        assert s.validate()


class TestCrearReservaSchema:
    def test_valido(self):
        s = CrearReservaSchema(
            id_espacio=1, curso_nombre="Matemáticas", horario="08:00-10:00", fecha="2026-06-01"
        )
        assert s.validate() == []

    def test_id_espacio_invalido(self):
        s = CrearReservaSchema(id_espacio=0, curso_nombre="Mat", horario="08:00", fecha="2026-01-01")
        assert "El ID del espacio debe ser un número positivo" in s.validate()


class TestMensajeChatSchema:
    def test_valido(self):
        s = MensajeChatSchema(mensaje="Hola, necesito un laboratorio")
        assert s.validate() == []

    def test_vacio(self):
        s = MensajeChatSchema(mensaje="")
        assert s.validate() != []


class TestCrearEspacioSchema:
    def test_valido(self):
        s = CrearEspacioSchema(
            nombre="Lab 101", id_tipo=1, ubicacion="Edificio A", capacidad=30
        )
        assert s.validate() == []

    def test_capacidad_invalida(self):
        s = CrearEspacioSchema(
            nombre="Lab", id_tipo=1, ubicacion="A", capacidad=-1
        )
        assert s.validate() != []


class TestCambiarEstadoSchema:
    def test_valido(self):
        s = CambiarEstadoSchema(id_espacio=1, estado="MANTENIMIENTO")
        assert s.validate() == []

    def test_estado_invalido(self):
        s = CambiarEstadoSchema(id_espacio=1, estado="INEXISTENTE")
        assert s.validate() != []
