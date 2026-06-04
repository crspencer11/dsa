def aggregate_minutes(events: list[dict]) -> dict[str, int]:
    final = {}

    for event in events:
        customer = event["customer_id"]

        if customer in final:
            final[customer] += event["minutes"]
        else:
            final[customer] = event["minutes"]

    return final


print(
    aggregate_minutes(
        [
            {
                "customer_id": "A",
                "minutes": 5,
            },
            {
                "customer_id": "A",
                "minutes": 10,
            },
            {
                "customer_id": "B",
                "minutes": 7,
            },
        ]
    )
)