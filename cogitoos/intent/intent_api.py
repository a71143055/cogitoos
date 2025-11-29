from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class Intent:
    type: str
    goal: str
    context: Dict[str, Any] = field(default_factory=dict)
    boundaries: Dict[str, str] = field(default_factory=dict)

class IntentAPI:
    def __init__(self, self_model, memory, privacy_governor):
        self.self_model = self_model
        self.memory = memory
        self.privacy_governor = privacy_governor

    def create_intent(self, type_: str, goal: str, context: Dict[str, Any], boundaries: Dict[str, str]) -> Intent:
        intent = Intent(type=type_, goal=goal, context=context, boundaries=boundaries)
        self.memory.trace.record_intent(intent)
        return intent
