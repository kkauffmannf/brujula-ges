from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    llm_provider: Literal["groq", "ollama", "fake"] = "groq"
    llm_model: str = "openai/gpt-oss-120b"
    groq_api_key: SecretStr | None = None
