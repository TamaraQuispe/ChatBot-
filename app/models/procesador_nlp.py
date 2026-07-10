import json
import time
import re
from typing import Optional
from config.database import Database
from core.logger import get_logger

logger = get_logger("nlp")


class ProcesadorNLP:
    def __init__(self, db: Database):
        self.db = db
        self.modelo = "reglas-v1"

    def procesar(self, id_usuario: int, prompt: str) -> dict:
        t0 = time.time()
        try:
            prompt_lower = prompt.lower().strip()
            intencion = self._detectar_intencion(prompt_lower)
            entidades = self._extraer_entidades(prompt_lower)

            if intencion == "reservar":
                accion = "reservar"
            elif intencion == "listar_reservas":
                accion = "listar"
            elif intencion == "cancelar":
                accion = "cancelar"
            else:
                accion = "consulta"

            resultado = {
                "intencion": intencion,
                "accion": accion,
                "entidades": entidades,
            }

            self._guardar_log(id_usuario, prompt, intencion, entidades, resultado, t0)
            return resultado
        except Exception as e:
            logger.error(f"Error procesando NLP: {e}")
            return {"intencion": "consulta", "accion": "consulta", "entidades": {}}

    def _detectar_intencion(self, texto: str) -> str:
        patrones_reservar = [
            r"reservar", r"apartar", r"agendar", r"quiero.*aula", r"necesito.*espacio",
            r"ocupar", r"separar", r"pedir.*sal[oó]n", r"solicitar.*aula",
            r"busco.*aula", r"hay.*disponible", r"mu[eé]strame.*aula",
        ]
        patrones_listar = [
            r"mis reservas", r"mis.*apartados", r"qu[eé] reservas.*tengo",
            r"listar.*reservas", r"ver.*reservas",
        ]
        patrones_cancelar = [
            r"cancelar", r"anular", r"eliminar.*reserva",
        ]

        for p in patrones_reservar:
            if re.search(p, texto):
                return "reservar"
        for p in patrones_listar:
            if re.search(p, texto):
                return "listar_reservas"
        for p in patrones_cancelar:
            if re.search(p, texto):
                return "cancelar"
        return "consulta_general"

    def _extraer_entidades(self, texto: str) -> dict:
        entidades = {}
        patron_curso = r"(?:curso|materia|asignatura)\s*(?:de\s*)?([a-zA-ZÀ-ÿ\s]{3,50})"
        m = re.search(patron_curso, texto)
        if m:
            entidades["curso"] = m.group(1).strip()

        patron_tipo = r"(?:aula|sal[oó]n|espacio|laboratorio|sala)\s*(?:de\s*)?(?:c[oó]mputo|te[oó]rica|pr[aá]ctica|lab)"
        m = re.search(patron_tipo, texto)
        if m:
            raw = m.group(0)
            if "cómputo" in raw or "computo" in raw:
                entidades["tipo_espacio"] = "COMPUTO"
            elif "teórica" in raw or "teorica" in raw:
                entidades["tipo_espacio"] = "TEORICA"
            elif "lab" in raw:
                entidades["tipo_espacio"] = "LABORATORIO"

        patron_hora = r"(\d{1,2}):?(\d{2})?\s*(?:a\.?m\.?|p\.?m\.?)?"
        m = re.search(patron_hora, texto)
        if m:
            entidades["hora_sugerida"] = m.group(0)

        return entidades

    def _guardar_log(self, id_usuario: int, prompt: str, intencion: str, entidades: dict, resultado: dict, t0: float):
        try:
            conn = self.db.obtener_conexion()
            cursor = conn.cursor()
            tiempo_ms = int((time.time() - t0) * 1000)
            cursor.execute(
                "INSERT INTO procesamiento_nlp (id_usuario, prompt_original, intencion_detectada, entidades_encontradas, resultado_json, modelo_usado, tiempo_procesamiento_ms) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (id_usuario, prompt, intencion, json.dumps(entidades), json.dumps(resultado), self.modelo, tiempo_ms)
            )
            conn.commit()
            conn.close()
        except Exception as e:
            logger.warning(f"No se pudo guardar log NLP: {e}")

    @staticmethod
    def crear_tabla(db: Database):
        try:
            conn = db.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS procesamiento_nlp (
                    id_procesamiento SERIAL PRIMARY KEY,
                    id_usuario INTEGER NOT NULL,
                    prompt_original TEXT NOT NULL,
                    intencion_detectada VARCHAR(255),
                    entidades_encontradas JSONB,
                    resultado_json JSONB,
                    modelo_usado VARCHAR(100),
                    tiempo_procesamiento_ms INTEGER,
                    fecha_creacion TIMESTAMP DEFAULT NOW(),
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
                );
            """)
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Error creando tabla procesamiento_nlp: {e}")
