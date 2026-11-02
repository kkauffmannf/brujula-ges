from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

Provider = Literal["groq", "ollama", "gemini", "fake"]

DEFAULT_MODELS: dict[Provider, str] = {
    "groq": "openai/gpt-oss-120b",
    "ollama": "qwen2.5:7b",
    "gemini": "gemini-3.5-flash-lite",
    "fake": "fake",
}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    llm_provider: Provider = "groq"
    llm_model: str | None = None
    groq_api_key: SecretStr | None = None
    gemini_api_key: SecretStr | None = None

    @property
    def modelo(self) -> str:
        return self.llm_model or DEFAULT_MODELS[self.llm_provider]
