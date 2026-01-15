from typing import List

def total_spend(customers: List[dict]) -> dict:
    """
    customers = [
        {"id": 1, "orders": [{"amount": 10}, {"amount": 5}]},
        {"id": 2, "orders": None},
        {"id": 3}
    ]
    """
    if not customers:
        return None
    output = {}
    for line_item in customers:
        customer = line_item['id']
        if customer not in output:
            if line_item.get('orders'):
                output[customer] = calc(line_item['orders'])
            else:
                output[customer] = 0
        else:
            output[customer] += calc(line_item['orders'])

    return output

def calc(input: List[dict]) -> int:
    total = 0
    for i in input:
        total += i['amount']
    return total
    

print(total_spend([
        {"id": 1, "orders": [{"amount": 10}, {"amount": 5}]},
        {"id": 2, "orders": None},
        {"id": 3}
    ]))
