data = "day-300/data.csv"

def generate(file: str):
    voters = set()
    candidates = {}

    with open(file, "r") as f:
        next(f)  # skip header if CSV
        for line in f:
            voter, candidate = line.strip().split(",")

            if voter in voters:
                print(f"Fraud detected: voter {voter}")
                continue

            voters.add(voter)
            candidates[candidate] = candidates.get(candidate, 0) + 1

    return top_three_candidates(candidates)


def top_three_candidates(candidates: dict):
    return sorted(
        candidates,
        key=candidates.get,
        reverse=True
    )[:3]


generate(data)