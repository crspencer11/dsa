def clean_data(orders: list[dict]) -> dict[str, float]:
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
    seen = {}
    result = {}

    for order in orders:
        if order.get("status", "").lower() != "paid":
            continue

        order_id = order.get("order_id")
        if order_id in seen:
            continue

        amount = convert_amount(order.get("amount"))
        if amount is None:
            continue

        customer = order.get("customer", "").strip().lower()

        seen[order_id] = True
        result[customer] = result.get(customer, 0.0) + amount

    return result

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

def total_spending(orders, customers):
    """
    orders = [
        {"order_id": "A1", "customer_id": 1, "amount": 10},
        {"order_id": "A2", "customer_id": 2, "amount": 20},
        {"order_id": "A3", "customer_id": 1, "amount": 5},
    ]

    customers = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]

    output:
    {
        "Alice": 15,
        "Bob": 20
    }
    """
    customer_lookup = {c["id"]: c["name"] for c in customers}
    totals = {}

    for order in orders:
        cid = order.get("customer_id")
        amount = order.get("amount")

        if cid not in customer_lookup:
            continue

        if not isinstance(amount, (int, float)):
            continue

        name = customer_lookup[cid]
        totals[name] = totals.get(name, 0) + amount

    return totals

print(total_spending(
    orders = [
        {"order_id": "A1", "customer_id": 1, "amount": 10},
        {"order_id": "A2", "customer_id": 2, "amount": 20},
        {"order_id": "A3", "customer_id": 1, "amount": 5},
    ],
    customers = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
))