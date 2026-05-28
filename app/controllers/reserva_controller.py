from app.models.espacio import EspacioAcademico
from app.models.reserva import Reserva
from core.logger import get_logger
from core.utils import escapar

logger = get_logger("reserva")


class ReservaController:
    def __init__(self, db):
        self.espacio_model = EspacioAcademico(db)
        self.reserva_model = Reserva(db)

    def buscar_disponibilidad(self, palabra_clave: str):
        try:
            if not palabra_clave or len(palabra_clave) > 500:
                return []
            palabra_clave = escapar(palabra_clave.strip().lower())
            tipo = "COMPUTO" if "computo" in palabra_clave or "cómputo" in palabra_clave else "TEORICA"
            return self.espacio_model.buscar_disponibles(tipo)
        except Exception as e:
            logger.error(f"Error buscando disponibilidad: {str(e)}")
            return []

    def procesar_reserva(self, id_usuario: int, curso: str, id_espacio: int, horario: str):
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
            exito = self.reserva_model.crear(id_usuario, curso, id_espacio, horario)
            if exito:
                self.espacio_model.ocupar(id_espacio)
                logger.info(f"Reserva creada: espacio={id_espacio}, usuario={id_usuario}")
            return exito
        except Exception as e:
            logger.error(f"Error al procesar reserva: {str(e)}")
            return False
