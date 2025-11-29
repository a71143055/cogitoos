from typing import Dict
from ..memory.trace import Trace

class DocEditorApp:
    def __init__(self, trace: Trace):
        self.trace = trace

    def explain(self) -> Dict:
        return {
            "because": ["사용자 목표: 작성", "지연 민감: 낮음", "온디바이스 우선"],
            "alternatives": ["Markdown", "RichText"],
            "impact": {"energy": "low", "time": "instant"}
        }

    def run(self) -> None:
        self.trace.record_task("doc_edit", "start", {"mode": "compose"})
        # Simulate work
        text = "오늘의 생각을 정리합니다..."
        # Persist snapshot (omitted heavy IO)
        self.trace.record_task("doc_edit", "finish", {"chars": len(text)})
        print("[doc_editor] 문서 작성 완료")
