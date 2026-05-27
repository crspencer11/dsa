from collections import defaultdict

def fun(dependencies: list[tuple[str, str]], start: str):

    def build_graph(dependencies):
        graph = defaultdict(list)
        for src, dst in dependencies:
            graph[src].append(dst)

        return graph

    graph = build_graph(dependencies)
    final = []
    seen = set()

    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                final.append(neighbor)

                dfs(neighbor)

    dfs(start)

    return final


print(
    fun(
        dependencies=[
            ("raw_users", "stg_users"),
            ("raw_users", "audit_users"),
            ("stg_users", "dim_users"),
            ("dim_users", "daily_metrics"),
            ("audit_users", "fraud_metrics"),
        ],
        start="raw_users",
    )
)