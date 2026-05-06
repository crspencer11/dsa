
import heapq

def normalize_optimal(logs: list[str], k: int):
    """
    Given a list of log entries (strings), return the most frequent K normalized paths, 
    where normalization removes query params and treats case-insensitively.

    logs = [
        "/home?user=1",
        "/Home",
        "/about",
        "/home?ref=google",
        "/ABOUT",
        "/home"
    ]
    k = 2

    output: ["/home", "/about"]
    """
    counts = {}

    for log in logs:
        path = log.split('?')[0].lower()
        counts[path] = counts.get(path, 0) + 1

    heap = []
    for path, freq in counts.items():
        heapq.heappush(heap, (freq, path))
        if len(heap) > k:
            heapq.heappop(heap)

    result = []
    while heap:
        freq, path = heapq.heappop(heap)
        result.append(path)

    return result[::-1]
