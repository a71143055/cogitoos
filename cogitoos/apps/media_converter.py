from typing import Dict
from ..memory.trace import Trace

class MediaConverterApp:
    def __init__(self, trace: Trace):
        self.trace = trace

    def explain(self) -> Dict:
        return {
            "because": ["목표: 압축률 최대, 품질 유지", "하드웨어 가속 가능"],
            "alternatives": ["HEVC", "VP9"],
            "impact": {"energy": "medium+", "time": "12min"}
        }

    def run(self) -> None:
        self.trace.record_task("media_convert", "start", {"codec": "AV1"})
        # Simulate heavy work
        print("[media_converter] 변환 중... (모사)")
        self.trace.record_task("media_convert", "finish", {"files": 42})
        print("[media_converter] 변환 완료")
