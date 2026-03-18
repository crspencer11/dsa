from datetime import datetime, timedelta, date

def find_available_slots(slots: list[set], booked: dict[set]):
    """
    slots = [
        ("2026-04-02", "09:00"),
        ("2026-04-02", "10:00"),
        ("2026-04-02", "11:00"),
    ]
    booked = {
        ("2026-04-02", "10:00")
    }
    """
    available = []
    for slot in slots:
        time_obj = datetime.strptime(slot[1], "%H:%M").time()
        dt_object = datetime.combine(date.today(), time_obj)
        minutes_to_add = 30
        updated_dt = dt_object + timedelta(minutes=minutes_to_add)
        if slot not in booked and updated_dt not in booked:
            available.append(slot)
    return available


slots = [
    ("2026-04-02", "09:00"),
    ("2026-04-02", "10:00"),
    ("2026-04-02", "11:00"),
    ("2026-04-02", "11:10"),
]
booked = {
    ("2026-04-02", "10:00"),
    ("2026-04-02", "10:50")
}

print(find_available_slots(slots, booked))