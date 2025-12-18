def hamiltonian(strArr) -> str:
    vertices = strArr[0][1:-1].split(",")
    edges = strArr[1][1:-1].split(",")
    path = strArr[2][1:-1].split(",")
    graph = {v: set() for v in vertices}

    for edge in edges:
        a, b = edge.split("-")
        graph[a].add(b)
        graph[b].add(a)
    # check all vertices used exactly once
    if set(path) != set(vertices):
        for v in vertices:
            if v not in path:
                return v
            
    for i in range(len(path)):
        curr = path[i]
        nxt = path[(i + 1) % len(path)]
        if nxt not in graph[curr]:
            return curr
    return "yes"