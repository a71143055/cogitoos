from .config import SystemConfig
from .utils.event_bus import EventBus
from .memory.trace import Trace
from .memory.persistence import Persistence
from .self_model.store import SelfModel
from .self_model.policies import Policies
from .privacy.governor import PrivacyGovernor
from .kernel.scheduler import IntentAwareScheduler
from .kernel.task import Task
from .intent.intent_api import IntentAPI
from .intent.interpreter import IntentInterpreter
from .shell.experience import ExperienceShell
from .shell.justify_panel import JustifyPanel
from .apps.doc_editor import DocEditorApp
from .apps.media_converter import MediaConverterApp
from .apps.communicator import CommunicatorApp

def bootstrap():
    cfg = SystemConfig()
    bus = EventBus()
    trace = Trace(cfg)
    store = SelfModel()
    policies = Policies(energy_mode="balanced", privacy_mode="balanced")
    privacy = PrivacyGovernor(mode=policies.privacy_mode)
    persist = Persistence()

    # Services
    scheduler = IntentAwareScheduler(self_model=store, privacy_governor=privacy)
    intent_api = IntentAPI(self_model=store, memory=type("Mem", (), {"trace": trace}), privacy_governor=privacy)
    interpreter = IntentInterpreter(self_model=store, privacy_governor=privacy)
    shell = ExperienceShell(self_model=store, trace=trace)

    # Apps
    apps = {
        "compose": DocEditorApp(trace),
        "convert": MediaConverterApp(trace),
        "communicate": CommunicatorApp(trace),
    }

    return {
        "cfg": cfg, "bus": bus, "trace": trace, "store": store, "policies": policies,
        "privacy": privacy, "persist": persist, "scheduler": scheduler,
        "intent_api": intent_api, "interpreter": interpreter, "shell": shell, "apps": apps
    }

def submit_intent(env, type_, goal, context, boundaries):
    # Apply policy budgets
    energy = env["policies"].apply_energy_budget(boundaries)
    privacy = env["policies"].apply_privacy_budget(boundaries)
    enriched = dict(boundaries, energy=energy, privacy=privacy)

    intent = env["intent_api"].create_intent(type_, goal, context, enriched)
    env["shell"].announce_intent(intent)
    env["store"].update_focus(type_)

    # Justification
    app = env["apps"].get(type_)
    explanation = app.explain() if app else {"because": ["기본 경로"], "alternatives": [], "impact": {}}
    summary = JustifyPanel.summarize(f"{type_}:{goal}", explanation)
    print(summary)
    env["trace"].record_decision("intent_explained", explanation)

    # Create task
    task = Task(
        name=f"{type_}_task",
        intent_type=type_,
        resources={"energy": enriched["energy"], "privacy": enriched["privacy"]},
        run=app.run if app else (lambda: print("[noop]")),
    )
    env["scheduler"].submit(task)

def demo_run():
    env = bootstrap()
    env["shell"].show_home()

    # Sample intents
    submit_intent(env, "compose", "아이디어 작성", {"doc": "notes.md"}, {"energy": "low", "privacy": "strict"})
    submit_intent(env, "convert", "사진 압축", {"src": "/Photos/Trip"}, {"energy": "medium", "privacy": "balanced"})
    submit_intent(env, "communicate", "팀 대화", {"room": "general"}, {"energy": "medium", "privacy": "open"})

    print("\n=== 스케줄러 실행 ===")
    env["scheduler"].run_all()

    print("\n=== 트레이스 샘플 ===")
    print(env["privacy"].explain())
    print(env["store"].snapshot())
    print(env["persist"].snapshot())

if __name__ == "__main__":
    demo_run()
