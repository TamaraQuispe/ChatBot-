"""Validación de operaciones de administración."""

from app.validators.base import ValidationRule, validate


def validate_crear_espacio(data: dict) -> list:
    rules = [
        ValidationRule("nombre", required=True, min_length=2, max_length=100),
        ValidationRule("id_tipo", required=True, type_=int, min_value=1),
        ValidationRule("ubicacion", required=True, min_length=2, max_length=200),
        ValidationRule("capacidad", required=True, type_=int, min_value=1),
    ]
    return validate(data, rules)


def validate_cambiar_estado(data: dict) -> list:
    rules = [
        ValidationRule("id_espacio", required=True, type_=int, min_value=1),
        ValidationRule("estado", required=True, min_length=1, max_length=20),
    ]
    return validate(data, rules)
