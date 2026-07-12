"""Validación base reutilizable."""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ValidationRule:
    field: str
    required: bool = False
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    pattern: Optional[str] = None
    type_: Optional[type] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None


def validate(data: dict, rules: list[ValidationRule]) -> list:
    errors = []
    for rule in rules:
        value = data.get(rule.field)
        if rule.required and not value and value != 0 and value is not False:
            errors.append(f"{rule.field} es requerido")
            continue
        if value is None or value == "":
            continue
        str_value = str(value)
        if rule.min_length and len(str_value) < rule.min_length:
            errors.append(f"{rule.field} debe tener al menos {rule.min_length} caracteres")
        if rule.max_length and len(str_value) > rule.max_length:
            errors.append(f"{rule.field} no debe exceder {rule.max_length} caracteres")
        if rule.pattern and not re.match(rule.pattern, str_value):
            errors.append(f"{rule.field} tiene formato inválido")
        if rule.type_:
            try:
                rule.type_(value)
            except (ValueError, TypeError):
                errors.append(f"{rule.field} debe ser de tipo {rule.type_.__name__}")
        if rule.min_value is not None:
            try:
                if float(value) < rule.min_value:
                    errors.append(f"{rule.field} debe ser mayor o igual a {rule.min_value}")
            except (ValueError, TypeError):
                pass
        if rule.max_value is not None:
            try:
                if float(value) > rule.max_value:
                    errors.append(f"{rule.field} debe ser menor o igual a {rule.max_value}")
            except (ValueError, TypeError):
                pass
    return errors


def validate_json_body(content_length: int, body: bytes) -> Optional[dict]:
    import json
    if content_length == 0:
        return None
    try:
        return json.loads(body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        return None
