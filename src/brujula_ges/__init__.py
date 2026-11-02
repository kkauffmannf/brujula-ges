import sys

from openai import APIConnectionError

from brujula_ges.app import responder
from brujula_ges.config import Settings
from brujula_ges.factory import build_chat_model


def main() -> None:
    pregunta = " ".join(sys.argv[1:]) or "¿Qué es el GES?"
    settings = Settings()
    llm = build_chat_model(settings)
    try:
        print(responder(pregunta, llm))
    except APIConnectionError:
        sys.exit(f"No pude conectarme al proveedor '{settings.llm_provider}'")
