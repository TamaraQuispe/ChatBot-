"""Validación del chatbot."""

from app.validators.base import ValidationRule, validate


def validate_chat_message(data: dict) -> list:
    rules = [
        ValidationRule("mensaje", required=True, min_length=1, max_length=2000),
    ]
    return validate(data, rules)
