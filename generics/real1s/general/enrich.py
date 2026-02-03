from typing import List

def enrich(events, users: List[dict]):
    """ input:
    events = [
        {"id": "e1", "user_id": "u1", "ts": 3},
        {"id": "e2", "user_id": "u2", "ts": 1},
        {"id": "e3", "user_id": "u1", "ts": 5},
    ]

    users = [
        {"id": "u1", "name": "Alice"},
        {"id": "u2", "name": "Bob"},
    ]

    output:
    [
        {"event_id": "e2", "user": "Bob", "ts": 1},
        {"event_id": "e1", "user": "Alice", "ts": 3},
        {"event_id": "e3", "user": "Alice", "ts": 5},
    ]
    """
    output = []
    lookup = create_lookup(users)
    for event in events:
        user = lookup.get(event.get("user_id"))
        if user:
            item = {
                'event_id': event['id'],
                'user': lookup[event['user_id']]['name'],
                'ts': event['ts']
            }
            output.append(item)
    output_ts_sorted = sorted(output, key=lambda output: output['ts'])
    return output_ts_sorted

def create_lookup(users: List[dict]):
    return {user['id']: user for user in users}

events = [
        {"id": "e1", "user_id": "u1", "ts": 3},
        {"id": "e2", "user_id": "u2", "ts": 1},
        {"id": "e3", "user_id": "u1", "ts": 5},
    ]

users = [
    {"id": "u1", "name": "Alice"},
    {"id": "u2", "name": "Bob"},
]
print(enrich(events, users))

def enrich_floats(events: List[dict]) -> List[dict]:
    """input:
    events = [
        {"source": "stripe", "amount_cents": 1200, "user_id": "u1"},
        {"source": "paypal", "amount": "15.50", "user": {"id": "u2"}},
        {"source": "stripe", "amount_cents": None, "user_id": "u3"},
    ]
    output:
    [
        {"user_id": "u1", "amount_usd": 12.00},
        {"user_id": "u2", "amount_usd": 15.50},
    ]    
    """
    intermediate = {}
    for event in events:
        if "user" in event.keys():
            print(True)
    #         user = event['user_id']
    #     if user in intermediate:
    #         intermediate[user].append(event['amount_cents'])

    #     else:
    #         intermediate[user] = [event['amount_cents']]

    # output = []
    # for k, v in intermediate:
    #     output[
    #         {
    #             'user_id': k,
    #             'amount_usd': sum(v) / 10
    #         }
    #     ]
    return [{}]

print(enrich_floats(events = [
        {"source": "stripe", "amount_cents": 1200, "user_id": "u1"},
        {"source": "paypal", "amount": "15.50", "user": {"id": "u2"}},
        {"source": "stripe", "amount_cents": None, "user_id": "u3"},
    ],
    ))
