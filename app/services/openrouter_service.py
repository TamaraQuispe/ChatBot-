import requests
from app.logger import get_logger
from app.settings import settings

logger = get_logger("openrouter")


class OpenRouterService:
    def __init__(self, model="openrouter/free"):
        self.api_key = settings.OPENROUTER_API_KEY
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY no definida.")
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = model

    def consultar(self, prompt: str, contexto: str | None = None) -> str:
        system = """Eres un asistente academico de la UTP.
Ayudas a docentes a buscar y reservar aulas.
Disponibilidad actual: {contexto}
Responde en espanol, se conciso."""

        messages = [
            {"role": "system", "content": system.format(contexto=contexto or "Sin datos")},
            {"role": "user", "content": prompt}
        ]

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://utp-reservas.vercel.app",
            "X-Title": "UTP Reservas"
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": 500
        }

        response = requests.post(self.api_url, headers=headers, json=payload, timeout=60)
        result = response.json()

        logger.info(f"OpenRouter HTTP {response.status_code}, model: {result.get('model')}")

        if response.status_code != 200:
            err = result.get("error", {})
            msg = err.get("message", str(result))
            logger.error(f"Error OpenRouter ({response.status_code}): {msg}")
            raise Exception(f"Error OpenRouter ({response.status_code}): {msg}")

        if "choices" in result and len(result["choices"]) > 0:
            msg = result["choices"][0].get("message", {})
            content = msg.get("content")
            if content:
                return content

            reasoning = msg.get("reasoning")
            if reasoning:
                import re
                quoted = re.findall(r'"([^"]*)"', reasoning)
                if quoted:
                    return quoted[-1]
                segments = reasoning.rsplit(":", 1)
                if len(segments) > 1:
                    return segments[-1].strip().strip('"\'.,!?')
                return reasoning.strip()

            if msg.get("refusal"):
                raise Exception(f"OpenRouter rechazo: {msg['refusal']}")

        logger.error(f"Respuesta inesperada de OpenRouter: {result}")
        raise Exception(f"Error OpenRouter: respuesta sin choices: {result}")
