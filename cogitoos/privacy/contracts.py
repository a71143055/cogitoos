from dataclasses import dataclass

@dataclass
class BoundaryContract:
    energy: str  # low | medium | high
    privacy: str  # strict | balanced | open

    def as_dict(self):
        return {"energy": self.energy, "privacy": self.privacy}
