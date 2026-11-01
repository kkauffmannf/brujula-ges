from typing import Protocol


class ChatModel(Protocol):
    def complete(self, prompt: str, *, system: str | None = None) -> str: ...
