from typing import Callable, Dict, List, Any
from collections import defaultdict

class EventBus:
    def __init__(self) -> None:
        self._subs: Dict[str, List[Callable[[Any], None]]] = defaultdict(list)

    def subscribe(self, event: str, handler: Callable[[Any], None]) -> None:
        self._subs[event].append(handler)

    def publish(self, event: str, payload: Any) -> None:
        for h in list(self._subs.get(event, [])):
            try:
                h(payload)
            except Exception as e:
                # Swallow to keep bus resilient
                print(f"[EventBus] handler error on {event}: {e}")
