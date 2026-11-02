"""Model wrapper. Everything else calls only these functions.
Stand-ins for now; swap in Muse Spark / Muse Spark Open / Muse Voice Transcribe later."""


def answer(question: str, facts: list[str]) -> str:
    """Big model: answer a new question from owner-approved facts."""
    raise NotImplementedError


def adapt(stored_answer: str, new_question: str) -> str:
    """Small model: rephrase a stored answer for a new customer's question."""
    raise NotImplementedError


def transcribe(audio_path: str) -> str:
    """Owner voice note -> text."""
    raise NotImplementedError
