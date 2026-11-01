from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam


class OpenAICompatibleChatModel:
    def __init__(self, *, base_url: str, api_key: str, model: str) -> None:
        self._client = OpenAI(base_url=base_url, api_key=api_key)
        self._model = model

    def complete(self, prompt: str, *, system: str | None = None) -> str:
        messages: list[ChatCompletionMessageParam] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = self._client.chat.completions.create(model=self._model, messages=messages)
        content = response.choices[0].message.content
        if content is None:
            raise RuntimeError("El modelo no devolvió texto")
        return content
