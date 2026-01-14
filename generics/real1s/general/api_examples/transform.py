from typing import List

def transform_response(api_data: dict[List]) -> List[dict]:
    """
    api_data = {
        "customers": [
            {"id": 1, "orders": [{"amount": 50}, {"amount": 30}]},
            {"id": 2, "orders": []}
        ]
    }

    Return:
    [
        {"customer_id": 1, "total_spent": 80},
        {"customer_id": 2, "total_spent": 0}
    ]
    """
    output = []
    for customer in api_data['customers']:
        total_spent = 0
        for order in customer['orders']:
            total_spent +=  order['amount']
        output.append(
            {
                "customer_id": customer['id'],
                'total_spent': total_spent,
            }
        )
    return output
        

print(transform_response({
        "customers": [
            {"id": 1, "orders": [{"amount": 50}, {"amount": 30}]},
            {"id": 2, "orders": []}
        ]
    }))

            
