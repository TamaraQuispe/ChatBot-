"""Validación de reservas."""

from app.validators.base import ValidationRule, validate


def validate_crear_reserva(data: dict) -> list:
    rules = [
        ValidationRule("id_espacio", required=True, type_=int, min_value=1),
        ValidationRule("curso_nombre", required=True, min_length=2, max_length=200),
        ValidationRule("horario", required=True, min_length=1, max_length=50),
        ValidationRule("fecha", required=True, min_length=10, max_length=10),
    ]
    return validate(data, rules)


def validate_cancelar_reserva(data: dict) -> list:
    rules = [
        ValidationRule("id_reserva", required=True, type_=int, min_value=1),
    ]
    return validate(data, rules)
