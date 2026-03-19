def find_avg_resolution(events: list[dict]) -> float:
    n = len(events)
    total_time = 0
    for event in events:
        time = event.get('time')
        total_time += time
    return total_time // n

events = [
  {"time": 1, "ticket_id": 10, "type": "opened"},
  {"time": 2, "ticket_id": 11, "type": "opened"},
  {"time": 4, "ticket_id": 10, "type": "resolved"},
  {"time": 5, "ticket_id": 11, "type": "resolved"},
]
print(find_avg_resolution(events))
