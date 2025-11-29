import json
import os
import time
from typing import Any
from dataclasses import asdict
from ..config import SystemConfig

class Trace:
    def __init__(self, cfg: SystemConfig):
        self.cfg = cfg
        os.makedirs(cfg.trace_dir, exist_ok=True)

    def _write(self, kind: str, payload: Any) -> None:
        ts = int(time.time() * 1000)
        path = os.path.join(self.cfg.trace_dir, f"{ts}.{kind}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    def record_intent(self, intent) -> None:
        self._write("intent", {"intent": asdict(intent)})

    def record_decision(self, label: str, reason: dict) -> None:
        self._write("decision", {"label": label, "reason": reason})

    def record_task(self, name: str, status: str, meta: dict) -> None:
        self._write("task", {"name": name, "status": status, "meta": meta})
