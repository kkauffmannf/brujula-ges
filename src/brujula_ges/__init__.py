import sys

from brujula_ges.app import responder
from brujula_ges.config import Settings
from brujula_ges.factory import build_chat_model


def main() -> None:
    pregunta = " ".join(sys.argv[1:]) or "¿Qué es el GES?"
    llm = build_chat_model(Settings())
    print(responder(pregunta, llm))
