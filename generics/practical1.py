from collections import defaultdict

def topological_sort_dfs(tasks, deps):
    """
    tasks = {
        "fetch_invoices": ["fetch_customers"],
        "fetch_customers": [],
        "generate_report": ["fetch_invoices"],
    }
    """
    graph = defaultdict(list)
    for task, dep in deps:
        graph[dep].append(task)

    visited = {}  # "unvisited", "visiting", "visited"
    order = []

    def dfs(node):
        if visited.get(node) == "visiting":
            raise ValueError("Cycle detected")
        if visited.get(node) == "visited":
            return

        visited[node] = "visiting"

        for child in graph[node]:
            dfs(child)

        visited[node] = "visited"
        order.append(node)

    for task in tasks:
        if task not in visited:
            dfs(task)

    order.reverse()
    return order
