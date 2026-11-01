from brujula_ges.adapters.fake import FakeChatModel
from brujula_ges.adapters.openai_compatible import OpenAICompatibleChatModel
from brujula_ges.config import Settings
from brujula_ges.ports import ChatModel


def build_chat_model(settings: Settings) -> ChatModel:
    if settings.llm_provider == "groq":
        if settings.groq_api_key is None:
            raise ValueError("Falta GROQ_API_KEY en el archivo .env")
        return OpenAICompatibleChatModel(
            base_url="https://api.groq.com/openai/v1",
            api_key=settings.groq_api_key.get_secret_value(),
            model=settings.llm_model,
        )
    if settings.llm_provider == "ollama":
        return OpenAICompatibleChatModel(
            base_url="http://localhost:11434/v1", api_key="ollama", model=settings.llm_model
        )
    return FakeChatModel()
