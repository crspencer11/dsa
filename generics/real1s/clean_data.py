
def clean_data(orders: list[dict]):
    """
    You’re given a list of order records from multiple systems:
    orders = [
        {"order_id": "A1", "customer": "alice", "amount": "10.50", "status": "paid"},
        {"order_id": "A1", "customer": "Alice ", "amount": 10.5, "status": "paid"},
        {"order_id": "A2", "customer": "bob", "amount": None, "status": "pending"},
        {"order_id": "A3", "customer": "BOB", "amount": "7", "status": "paid"},
    ]
    Return total paid revenue per normalized customer.
    Requirements:
        - Normalize customer names (case + whitespace)
        - Deduplicate orders by order_id
        - Ignore invalid/missing amounts

    output:
    {
        "alice": 10.5,
        "bob": 7.0
    }
    """
    output = {}
    mapped = {}
    for order in orders:
        status = order['status'].lower()
        amount = convert_amount(order['amount'])
        order_id = order['order_id']
        customer = order['customer'].lower()
        if status != 'paid' or not amount:
            continue
        if order_id not in mapped:
            mapped[order_id] = [customer, amount]
    
    for v in mapped.values():
        output[v[0]] = v[1]
    return output

def convert_amount(value):
    try:
        amount = float(value)
        if amount.is_integer():
            return int(amount)
        return amount
    except (ValueError, TypeError):
        return None


print(clean_data(orders = [
        {"order_id": "A1", "customer": "alice", "amount": "10.50", "status": "paid"},
        {"order_id": "A1", "customer": "Alice ", "amount": 10.5, "status": "paid"},
        {"order_id": "A2", "customer": "bob", "amount": None, "status": "pending"},
        {"order_id": "A3", "customer": "BOB", "amount": "7", "status": "paid"},
    ]))