def invert_mapping(map: dict):
    """
    Input: {"a": 1, "b": 2, "c": 1}
    Output: {1: ["a", "c"], 2: ["b"]}
    """
    output = {}
    for k, v in map.items():
        if v in output:
            output[v].append(k)
        else:
            output[v] = [k]
    return output

print(invert_mapping({"a": 1, "b": 2, "c": 1}))
