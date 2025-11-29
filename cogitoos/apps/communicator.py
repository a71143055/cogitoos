from typing import Dict
from ..memory.trace import Trace

class CommunicatorApp:
    def __init__(self, trace: Trace):
        self.trace = trace

    def explain(self) -> Dict:
        return {
            "because": ["실시간 응답 필요", "네트워크 품질: 양호(wifi)"],
            "alternatives": ["이메일", "메신저"],
            "impact": {"energy": "medium", "time": "real-time"}
        }

    def run(self) -> None:
        self.trace.record_task("communicate", "start", {"channel": "chat"})
        print("[communicator] 대화 중... (모사)")
        self.trace.record_task("communicate", "finish", {"messages": 5})
        print("[communicator] 대화 종료")
