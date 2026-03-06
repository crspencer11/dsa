from collections import defaultdict, deque

class MessageCounter:

    def __init__(self):
        self.events = deque()
        self.counts = defaultdict(int)

    def process_event(self, event, now):
        if event["event_type"] != "message_sent":
            return

        uid = event["user_id"]

        self.events.append(event)
        self.counts[uid] += 1

        # expire old events
        while self.events and now - self.events[0]["timestamp"] > 86400:
            old = self.events.popleft()
            self.counts[old["user_id"]] -= 1
