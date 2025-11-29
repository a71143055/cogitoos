import time
from contextlib import contextmanager

@contextmanager
def timebox(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        dur = (time.perf_counter() - start) * 1000
        print(f"[timebox] {label}: {dur:.2f}ms")
