def find_dependencies(dependencies: list[tuple[str, str]], start: str):
    """
    Inputs:
    dependencies = [
        ("raw_users", "stg_users"),
        ("stg_users", "dim_users"),
        ("dim_users", "daily_metrics"),
        ("raw_orders", "fct_orders"),
        ("fct_orders", "daily_metrics")
    ]

    start = "raw_users"

    Output:
    [
        "stg_users",
        "dim_users",
        "daily_metrics"
    ]
    """

    def build_graph(dependencies: list[tuple[str, str]]):
        graph = {}

        for src, dst in dependencies:
            graph[src] = dst

        return graph

    graph = build_graph(dependencies)

    final = []
    seen = set()

    while start in graph and start not in seen:
        seen.add(start)

        neighbor = graph[start]
        final.append(neighbor)

        start = neighbor

    return final


print(
    find_dependencies(
        dependencies=[
            ("raw_users", "stg_users"),
            ("stg_users", "dim_users"),
            ("dim_users", "daily_metrics"),
            ("raw_orders", "fct_orders"),
            ("fct_orders", "daily_metrics"),
        ],
        start="raw_users",
    )
)