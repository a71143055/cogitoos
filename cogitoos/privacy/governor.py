class PrivacyGovernor:
    """
    Policy guard for data movement and sensor access.
    """
    def __init__(self, mode: str = "balanced"):
        self.mode = mode  # strict | balanced | open

    def boundary_bonus(self, privacy_level: str) -> float:
        # Reward tasks that respect stricter privacy
        if privacy_level == "strict":
            return 0.5
        if privacy_level == "balanced":
            return 0.3
        return 0.1

    def allow_network(self) -> bool:
        if self.mode == "strict":
            return False
        return True

    def explain(self) -> dict:
        return {"mode": self.mode}
