from app.models.espacio import EspacioAcademico
from app.models.reserva import Reserva
from app.models.gestor_reservas import GestorReservas
from core.logger import get_logger
from core.utils import escapar

logger = get_logger("reserva")


class ReservaController:
    def __init__(self, db):
        self.espacio_model = EspacioAcademico(db)
        self.reserva_model = Reserva(db)
        self.gestor = GestorReservas(db)

    def buscar_disponibilidad(self, palabra_clave: str) -> list:
        try:
            if not palabra_clave or len(palabra_clave) > 500:
                return []
            palabra_clave = escapar(palabra_clave.strip().lower())
            if "computo" in palabra_clave or "cómputo" in palabra_clave:
                tipo = "COMPUTO"
            elif "laboratorio" in palabra_clave or "lab" in palabra_clave:
                tipo = "LABORATORIO"
            elif "teorica" in palabra_clave or "teórica" in palabra_clave or "aula" in palabra_clave:
                tipo = "TEORICA"
            else:
                tipo = "COMPUTO"
            return self.espacio_model.buscar_disponibles(tipo)
        except Exception as e:
            logger.error(f"Error buscando disponibilidad: {e}")
            return []

    def procesar_reserva(self, id_usuario: int, curso: str, id_espacio: int, horario: str, fecha: str = "2026-05-28") -> bool:
        try:
            if not isinstance(id_usuario, int) or id_usuario <= 0:
                return False
            if not isinstance(id_espacio, int) or id_espacio <= 0:
                return False
            if not curso or len(curso) > 255:
                curso = "Curso sin nombre"
            if not horario or len(horario) > 100:
                return False
            curso = escapar(curso.strip())
            horario = escapar(horario.strip())
            return self.gestor.crear_reserva(id_usuario, id_espacio, curso, horario, fecha)
        except Exception as e:
            logger.error(f"Error al procesar reserva: {e}")
            return False
