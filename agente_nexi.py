from google import genai
import config_inicial

class AgenteNexi:
    def __init__(self):
        self.client = genai.Client(api_key=config_inicial.API_KEY)
        self.resetear_chat()
        self.historial_bolsa = []
        self.intentos = 0

    def resetear_chat(self):
        """Limpia el historial en la nube de Google completamente."""
        self.chat = self.client.chats.create(
            model="gemini-2.5-flash",
            config={"system_instruction": (
                "Sos NEXI, Soporte IT. 1. Máximo 20 palabras. 2. Técnica y directa. "
                "3. Una pregunta por vez. 4. Si tras 3 intentos no se resuelve, decí 'ESCALAR'."
            )}
        )
        self.historial_bolsa = []
        self.intentos = 0