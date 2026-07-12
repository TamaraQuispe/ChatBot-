import os
import requests


class OpenRouterService:
    def __init__(self, model="openrouter/free"):
        self.api_key = os.environ.get("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY no definida.")
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = model

    def consultar(self, prompt, contexto=None):
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
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": 300
        }

        response = requests.post(self.api_url, headers=headers, json=payload, timeout=60)
        result = response.json()

        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        raise Exception(f"Error OpenRouter: {result}")
