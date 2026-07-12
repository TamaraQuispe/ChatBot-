"""Validación de autenticación."""

from app.validators.base import ValidationRule, validate


def validate_login(data: dict) -> list:
    rules = [
        ValidationRule("username", required=True, min_length=3, max_length=50),
        ValidationRule("password", required=True, min_length=1, max_length=128),
    ]
    return validate(data, rules)


def validate_register(data: dict) -> list:
    rules = [
        ValidationRule("username", required=True, min_length=3, max_length=50,
                       pattern=r"^[a-zA-Z0-9_]+$"),
        ValidationRule("password", required=True, min_length=6, max_length=128),
        ValidationRule("nombre", required=True, min_length=2, max_length=100),
        ValidationRule("correo", required=True, max_length=100,
                       pattern=r"^[^\s@]+@[^\s@]+\.[^\s@]+$"),
        ValidationRule("rol", required=False, max_length=20),
    ]
    return validate(data, rules)
