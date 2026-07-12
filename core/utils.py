"""Adapter: Utils legacy → nueva arquitectura."""

from app.utils import escapar, sanitizar, validar_username, validar_email, parse_int


def liberar_espacios_vencidos(db=None, horas_max=2):
    from app.utils import liberar_espacios_vencidos as _liberar
    return _liberar(horas_max)
