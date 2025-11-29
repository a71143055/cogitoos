from typing import Any, Dict, Optional

class Persistence:
    """
    Minimal in-memory persistence with snapshot hooks.
    """
    def __init__(self):
        self._state: Dict[str, Any] = {}

    def put(self, key: str, value: Any) -> None:
        self._state[key] = value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self._state.get(key, default)

    def snapshot(self) -> Dict[str, Any]:
        return dict(self._state)
