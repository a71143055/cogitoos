from dataclasses import dataclass, field
from typing import Dict

@dataclass
class SelfModel:
    battery_percent: int = 80
    thermal_ok: bool = True
    network: str = "wifi"  # none | cellular | wifi
    current_focus_intent: str = "compose"
    intent_weights: Dict[str, float] = field(default_factory=lambda: {
        "compose": 1.5, "convert": 1.0, "communicate": 1.2
    })

    def intent_weight(self, intent_type: str) -> float:
        return self.intent_weights.get(intent_type, 0.5)

    def energy_penalty(self, energy_level: str) -> float:
        base = {"low": 0.1, "medium": 0.3, "high": 0.7}.get(energy_level, 0.3)
        # Increase penalty when battery is low
        if self.battery_percent < 25:
            base += 0.4
        return base

    def update_focus(self, intent_type: str) -> None:
        self.current_focus_intent = intent_type

    def snapshot(self) -> Dict:
        return {
            "battery_percent": self.battery_percent,
            "thermal_ok": self.thermal_ok,
            "network": self.network,
            "focus": self.current_focus_intent,
        }
