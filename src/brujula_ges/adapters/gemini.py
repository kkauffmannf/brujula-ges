from google import genai


class GeminiChatModel:
    def __init__(self, *, api_key: str, model: str) -> None:
        self._client = genai.Client(api_key=api_key)
        self._model = model

    def complete(self, prompt: str, *, system: str | None = None) -> str:
        if system:
            interaction = self._client.interactions.create(
                model=self._model,
                input=prompt,
                system_instruction=system,
                generation_config={"thinking_level": "low"},
            )
        else:
            interaction = self._client.interactions.create(
                model=self._model, input=prompt, generation_config={"thinking_level": "low"}
            )

        # create() puede devolver una respuesta completa o un stream. No pedimos
        # stream, así que esperamos texto; si no llega, fallamos con un mensaje claro.
        texto = getattr(interaction, "output_text", None)
        if not isinstance(texto, str) or not texto:
            raise RuntimeError("Gemini no devolvió texto")
        return texto
