from typing import List

def sort_users(users: List[dict]) -> List[dict]:
    """
    users = [
        {"name": "Alice", "last_login": 1700000000},
        {"name": "Bob", "last_login": None}
    ]
    Sort by last_login desc, None values last
    """
    return sorted(users, key=lambda user: (user["last_login"] is None, -(user["last_login"] or 0)))

print(sort_users([
        {"name": "Alice", "last_login": 1700000000},
        {"name": "Bob", "last_login": None},
        {"name": "Mike", "last_login": 1700000001},
        {"name": "Bill", "last_login": 1690000000}
    ]))