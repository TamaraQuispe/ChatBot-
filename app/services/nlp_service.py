"""Servicio NLP - Procesamiento de lenguaje natural basado en reglas."""

import json
import time
import re
from app.logger import get_logger

logger = get_logger("nlp_service")


class NLPService:
    def __init__(self):
        self.modelo = "reglas-v1"

    def procesar(self, id_usuario: int, prompt: str) -> dict:
        t0 = time.time()
        try:
            prompt_lower = prompt.lower().strip()
            intencion = self._detectar_intencion(prompt_lower)
            entidades = self._extraer_entidades(prompt_lower)

            mapa_accion = {
                "reservar": "reservar",
                "listar_reservas": "listar",
                "cancelar": "cancelar",
            }
            accion = mapa_accion.get(intencion, "consulta")

            return {
                "intencion": intencion,
                "accion": accion,
                "entidades": entidades,
            }
        except Exception as e:
            logger.error(f"Error procesando NLP: {e}")
            return {"intencion": "consulta", "accion": "consulta", "entidades": {}}

    def _detectar_intencion(self, texto: str) -> str:
        patrones = {
            "reservar": [
                r"reservar", r"apartar", r"agendar", r"quiero.*aula",
                r"necesito.*espacio", r"ocupar", r"separar",
                r"pedir.*sal[oó]n", r"solicitar.*aula",
                r"busco.*aula", r"hay.*disponible", r"mu[eé]strame.*aula",
            ],
            "listar_reservas": [
                r"mis reservas", r"mis.*apartados", r"qu[eé] reservas.*tengo",
                r"listar.*reservas", r"ver.*reservas",
            ],
            "cancelar": [
                r"cancelar", r"anular", r"eliminar.*reserva",
            ],
        }
        for intencion, patrones_list in patrones.items():
            for p in patrones_list:
                if re.search(p, texto):
                    return intencion
        return "consulta_general"

    def _extraer_entidades(self, texto: str) -> dict:
        entidades = {}

        m_curso = re.search(
            r"(?:curso|materia|asignatura)\s*(?:de\s*)?([a-zA-ZÀ-ÿ\s]{3,50})",
            texto,
        )
        if m_curso:
            entidades["curso"] = m_curso.group(1).strip()

        m_tipo = re.search(
            r"(?:aula|sal[oó]n|espacio|laboratorio|sala)\s*(?:de\s*)?"
            r"(?:c[oó]mputo|te[oó]rica|pr[aá]ctica|lab)",
            texto,
        )
        if m_tipo:
            raw = m_tipo.group(0)
            if "cómputo" in raw or "computo" in raw:
                entidades["tipo_espacio"] = "COMPUTO"
            elif "teórica" in raw or "teorica" in raw:
                entidades["tipo_espacio"] = "TEORICA"
            elif "lab" in raw:
                entidades["tipo_espacio"] = "LABORATORIO"

        m_hora = re.search(r"(\d{1,2}):?(\d{2})?\s*(?:a\.?m\.?|p\.?m\.?)?", texto)
        if m_hora:
            entidades["hora_sugerida"] = m_hora.group(0)

        return entidades
