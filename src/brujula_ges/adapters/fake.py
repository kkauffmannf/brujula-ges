class FakeChatModel:
    def __init__(self, respuesta: str = "respuesta falsa") -> None:
        self.respuesta = respuesta
        self.llamadas: list[tuple[str, str | None]] = []

    def complete(self, prompt: str, *, system: str | None = None) -> str:
        self.llamadas.append((prompt, system))
        return self.respuesta
