from brujula_ges.ports import ChatModel

SYSTEM_PROMPT = (
    "Eres Brújula GES, un asistente que explica las Garantías Explícitas en Salud de Chile "
    "en lenguaje simple. No das diagnósticos ni consejos médicos."
)


def responder(pregunta: str, llm: ChatModel) -> str:
    return llm.complete(pregunta, system=SYSTEM_PROMPT)
