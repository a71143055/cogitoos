from cogitoos.self_model.store import SelfModel
from cogitoos.privacy.governor import PrivacyGovernor
from cogitoos.intent.interpreter import IntentInterpreter

def test_intent_interpret_defaults():
    interpreter = IntentInterpreter(SelfModel(), PrivacyGovernor())
    intent = interpreter.interpret({"type": "compose", "goal": "write"})
    assert intent.type == "compose"
    assert intent.boundaries["energy"] == "medium"
    assert intent.boundaries["privacy"] == "balanced"
