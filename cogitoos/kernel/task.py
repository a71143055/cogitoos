from dataclasses import dataclass, field
from typing import Callable, Dict, Any

@dataclass
class Task:
    name: str
    intent_type: str
    resources: Dict[str, Any]
    run: Callable[[], None]
    priority: float = field(default=0.0)

    def __post_init__(self):
        self.priority = float(self.priority)
