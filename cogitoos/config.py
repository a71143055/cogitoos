from dataclasses import dataclass

@dataclass(frozen=True)
class SystemConfig:
    name: str = "CogitoOS"
    version: str = "0.1.0"
    trace_dir: str = ".cogito_trace"
    default_energy_budget: str = "medium"  # low | medium | high
    default_privacy_mode: str = "balanced"  # strict | balanced | open
