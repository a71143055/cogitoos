from cogitoos.self_model.store import SelfModel
from cogitoos.privacy.governor import PrivacyGovernor
from cogitoos.kernel.scheduler import IntentAwareScheduler
from cogitoos.kernel.task import Task

def test_scheduler_prioritizes_intent():
    store = SelfModel()
    gov = PrivacyGovernor()
    sched = IntentAwareScheduler(store, gov)

    t1 = Task(name="compose", intent_type="compose", resources={"energy": "low", "privacy": "strict"}, run=lambda: None)
    t2 = Task(name="convert", intent_type="convert", resources={"energy": "high", "privacy": "balanced"}, run=lambda: None)
    sched.submit(t1)
    sched.submit(t2)

    # 'compose' should generally rank higher due to intent weight and privacy bonus vs energy penalty
    first = sched.next()
    assert first.name == "compose"
