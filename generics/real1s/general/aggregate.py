from typing import List

def aggregate(accounts: List[dict]) -> List[dict]:
    """input:
    accounts = [
        {"id": "a1", "transactions": [{"amount": 10}, {"amount": -5}]},
        {"id": "a2", "transactions": None},
    ]
    
    output:
    [
        {"id": "a1", "balance": 5},
        {"id": "a2", "balance": 0},
    ]
    """
    output = []
    for account in accounts:
        balance = 0
        transactions = account.get('transactions')
        if transactions:
            for amt in transactions:
                balance += amt.get('amount')
        line_item = {
            'id': account.get('id'),
            'balance': balance
        }
        output.append(line_item)
    sorted_output = sorted(output, key=lambda output: output.get('balance'), reverse=True)
    return sorted_output

print(aggregate(accounts = [
        {"id": "a1", "transactions": [{"amount": 10}, {"amount": -5}]},
        {"id": "a2", "transactions": None},
    ]))
