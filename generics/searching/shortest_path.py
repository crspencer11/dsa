import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # min-heap of (distance, node)
    pq = [(0, start)]
    visited = set()

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_node not in visited:
            visited.add(curr_node)

            for neighbor, weight in graph[curr_node].items():
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
source_vertex = 'A'

print(dijkstra(graph, source_vertex))
