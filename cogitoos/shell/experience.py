from typing import List
from ..intent.intent_api import Intent
from ..self_model.store import SelfModel
from ..memory.trace import Trace

class ExperienceShell:
    """
    Console-based goal-centric shell.
    """
    def __init__(self, self_model: SelfModel, trace: Trace):
        self.self_model = self_model
        self.trace = trace

    def show_home(self) -> None:
        snap = self.self_model.snapshot()
        print("\n=== CogitoOS Home ===")
        print(f"- Focus: {snap['focus']}")
        print(f"- Battery: {snap['battery_percent']}%")
        print(f"- Network: {snap['network']}\n")
        print("Goals:")
        goals: List[str] = ["compose", "convert", "communicate"]
        for idx, g in enumerate(goals, start=1):
            print(f"  {idx}. {g}")

    def announce_intent(self, intent: Intent) -> None:
        print(f"[shell] intent: {intent.type} → {intent.goal}")
        self.trace.record_decision("intent_announced", {
            "intent": intent.type, "goal": intent.goal, "boundaries": intent.boundaries
        })
