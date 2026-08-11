from collections import deque
from datetime import datetime

class RateLimiter:
    def __init__(self, window: int, requests_allowed: int):
        self.window = window
        self.requests_allowed = requests_allowed
        self.client_requests = {}

    def allow_request(self, client_id: str) -> bool:
        current_time = datetime.now()
        if client_id not in self.client_requests:
            self.client_requests[client_id] = deque()

        q = self.client_requests[client_id]

        # prune anything older than the window
        while q and (current_time - q[0]).total_seconds() > self.window:
            q.popleft()

        if len(q) < self.requests_allowed:
            q.append(current_time)
            return True

        return False
