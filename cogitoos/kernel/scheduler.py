import heapq
import time
from typing import List, Optional
from .task import Task

class IntentAwareScheduler:
    """
    Priority = base + intent_weight + boundary_bonus - energy_penalty
    Simulates CPU/I-O scheduling by prioritizing tasks according to user intent and self-model.
    """
    def __init__(self, self_model, privacy_governor):
        self.queue: List[tuple[float, int, Task]] = []
        self._counter = 0
        self.self_model = self_model
        self.privacy_governor = privacy_governor

    def submit(self, task: Task) -> None:
        score = self._score(task)
        self._counter += 1
        heapq.heappush(self.queue, (-score, self._counter, task))  # max-heap via negative
        print(f"[scheduler] submitted '{task.name}' score={score:.2f}")

    def _score(self, task: Task) -> float:
        intent_weight = self.self_model.intent_weight(task.intent_type)
        energy_penalty = self.self_model.energy_penalty(task.resources.get("energy", "medium"))
        boundary_bonus = self.privacy_governor.boundary_bonus(task.resources.get("privacy", "balanced"))
        base = 1.0
        return base + intent_weight + boundary_bonus - energy_penalty

    def next(self) -> Optional[Task]:
        if not self.queue:
            return None
        _, _, task = heapq.heappop(self.queue)
        return task

    def run_all(self) -> None:
        while self.queue:
            task = self.next()
            if not task:
                break
            print(f"[scheduler] running '{task.name}' (intent={task.intent_type})")
            try:
                start = time.perf_counter()
                task.run()
                dur = (time.perf_counter() - start) * 1000
                print(f"[scheduler] '{task.name}' done in {dur:.1f}ms")
            except Exception as e:
                print(f"[scheduler] task '{task.name}' error: {e}")
