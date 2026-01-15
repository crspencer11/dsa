from typing import List

def flatten(customers: List[dict]) -> List[dict]:
    """
    Return:
    [
        {"customer_id": 1, "amount": 10},
        {"customer_id": 1, "amount": 5}
    ]
    """
    output = [
        {
            'customer_orders': {
                'customer_id': customers[0]['customer_id'],
                'amount': customers[0]['amount']
            }
        }
    ]

    for i in range(1, len(customers)):
        customer = customers[i]
        if customer['customer_id'] in output['customer_orders']:
            output["customer_orders"]['amount'] += customer['amount']
        else:
            output['customer_orders']['customer_id'] = customer['amount']
    return output

print(flatten([
        {"customer_id": 1, "amount": 10},
        {"customer_id": 1, "amount": 5}
    ]))
