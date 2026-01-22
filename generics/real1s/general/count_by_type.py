from typing import List

def count_by_type(events: List[dict]):
    """
    events = [
        {"type": "click"},
        {"type": "view"},
        {"type": "click"}
    ]

    Return {"click": 2, "view": 1}
    """
    output ={
        events[0]['type']: 1
    }

    for i in range(1, len(events)):
        event_type = events[i]["type"]
        print(event_type)
        if event_type in output:
            output[event_type] += 1
        else:
            output[event_type] = 1
    return output

print(count_by_type([
        {"type": "click"},
        {"type": "view"},
        {"type": "click"}
    ]))
