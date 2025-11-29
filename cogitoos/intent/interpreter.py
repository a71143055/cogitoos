from typing import Dict, Any
from .intent_api import Intent

class IntentInterpreter:
    """
    Elevates raw input/context into structured intents.
    """
    def __init__(self, self_model, privacy_governor):
        self.self_model = self_model
        self.privacy_governor = privacy_governor

    def interpret(self, raw: Dict[str, Any]) -> Intent:
        type_ = raw.get("type", "unknown")
        goal = raw.get("goal", "unspecified")
        context = raw.get("context", {})
        boundaries = raw.get("boundaries", {"energy": "medium", "privacy": "balanced"})
        return Intent(type=type_, goal=goal, context=context, boundaries=boundaries)
