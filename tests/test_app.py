from brujula_ges.adapters.fake import FakeChatModel
from brujula_ges.app import SYSTEM_PROMPT, responder
from brujula_ges.config import Settings
from brujula_ges.factory import build_chat_model


def test_responder_usa_el_prompt_de_sistema() -> None:
    llm = FakeChatModel(respuesta="El GES es...")
    assert responder("¿Qué es el GES?", llm) == "El GES es..."
    assert llm.llamadas == [("¿Qué es el GES?", SYSTEM_PROMPT)]


def test_fabrica_entrega_el_falso() -> None:
    assert isinstance(build_chat_model(Settings(llm_provider="fake")), FakeChatModel)
