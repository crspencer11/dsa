"""
data = [
  {"id": 1, "email": " Alice@example.com ", "country": "US", "spend": "10"},
  {"id": 2, "email": "bob@example.com", "country": "us", "spend": "20"},
  {"id": 3, "email": "alice@example.com", "country": "US", "spend": None},
  {"id": 4, "email": "charlie@example.com", "country": "CA", "spend": "15"},
]

workflow = [
  {"type": "normalize"},
  {"type": "filter", "field": "country", "value": "us"},
  {"type": "dedupe", "key": "email"},
  {"type": "aggregate", "group_by": "email", "field": "spend"}
]

I want to:
1. normalize: email, country, spend
2. filter where row[field] == value
3. dedupe
4. aggregate: group_by, sum(field), ignore invalide(None, non-numeric, etc)

expected_output:
{
  "alice@example.com": 10.0,
  "bob@example.com": 20.0
}
"""
def run(workflow: list[dict], data: list[dict]):
    step_map = {
        "normalize": normalize,
        "filter": filter_step,
        "dedupe": dedupe,
        "aggregate": aggregate,
    }

    current = data
    for step in workflow:
        step_type = step["type"]
        fn = step_map[step_type]
        current = fn(current, step)

    return current

def normalize(data: list[dict]) -> list[dict]:
    output = []
    for d in data:
        new_row = dict(d)

        email = new_row.get("email")
        if isinstance(email, str):
            new_row["email"] = email.strip().lower()

        country = new_row.get("country")
        if isinstance(country, str):
            new_row["country"] = country.upper()

        spend = new_row.get("spend")
        try:
            new_row["spend"] = float(spend)
        except (TypeError, ValueError):
            new_row["spend"] = None

        output.append(new_row)

    return output

def filter_step(rows, config) -> list[dict]:
    field = config["field"]
    value = config["value"]
    return [r for r in rows if r.get(field) == value]

def dedupe(rows, config) -> list:
    key = config["key"]
    seen = set()
    out = []

    for r in rows:
        k = r.get(key)
        if k in seen:
            continue
        seen.add(k)
        out.append(r)

    return out

def aggregate(rows, config) -> dict[str, float]:
    group_by = config["group_by"]
    field = config["field"]

    result = {}
    for r in rows:
        key = r.get(group_by)
        val = r.get(field)

        if not isinstance(val, (int, float)):
            continue

        result[key] = result.get(key, 0.0) + val

    return result