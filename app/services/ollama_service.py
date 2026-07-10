import requests


class OllamaService:
    def __init__(self, model="llama3.2:3b", url="http://localhost:11434"):
        self.model = model
        self.url = url

    def consultar(self, prompt, contexto=None):
        system = """Eres un asistente academico de la UTP.
Ayudas a docentes a buscar y reservar aulas.
Disponibilidad actual: {contexto}
Responde en espanol, se conciso."""

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system.format(contexto=contexto or "Sin datos")},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }

        r = requests.post(f"{self.url}/api/chat", json=payload)
        return r.json()["message"]["content"]
