def backoff(attempt, base=0.5, cap=30.0):
    """Seconds to wait before retry number `attempt` (exponential, capped)."""
    return min(cap, base * 2 ** attempt)
