from typing import Dict

class JustifyPanel:
    """
    Renders reasons in compact natural language.
    """
    @staticmethod
    def summarize(label: str, reason: Dict) -> str:
        because = reason.get("because", [])
        alts = reason.get("alternatives", [])
        impact = reason.get("impact", {})
        parts = []
        if because:
            parts.append("이유: " + "; ".join(because))
        if alts:
            parts.append("대안: " + ", ".join(alts))
        if impact:
            parts.append(f"영향: energy={impact.get('energy')}, time={impact.get('time')}")
        return f"[왜?] {label} → " + " | ".join(parts) if parts else f"[왜?] {label}"
