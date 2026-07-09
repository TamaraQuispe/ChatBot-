from abc import ABC, abstractmethod
from typing import Optional


class IGestorReservas(ABC):
    @abstractmethod
    def crear_reserva(self, id_usuario: int, id_espacio: int, curso_nombre: str, horario: str, fecha: str) -> bool:
        pass

    @abstractmethod
    def cancelar_reserva(self, id_reserva: int) -> bool:
        pass

    @abstractmethod
    def listar_reservas_activas(self) -> list:
        pass

    @abstractmethod
    def reservas_por_usuario(self, id_usuario: int) -> list:
        pass
