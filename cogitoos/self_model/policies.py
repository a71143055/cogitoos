from dataclasses import dataclass
from typing import Dict

@dataclass
class Policies:
    energy_mode: str = "balanced"  # saver | balanced | performance
    privacy_mode: str = "balanced"  # strict | balanced | open

    def apply_energy_budget(self, boundaries: Dict[str, str]) -> str:
        requested = boundaries.get("energy", "medium")
        if self.energy_mode == "saver":
            return "low"
        if self.energy_mode == "performance":
            return "high"
        return requested

    def apply_privacy_budget(self, boundaries: Dict[str, str]) -> str:
        requested = boundaries.get("privacy", "balanced")
        if self.privacy_mode == "strict":
            return "strict"
        if self.privacy_mode == "open":
            return "open"
        return requested
