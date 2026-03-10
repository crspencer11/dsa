data = "day-300/data.csv"

class FraudDetector:
    def __init__(self):
        self.voters = set()
        self.candidates = {}

    def process_file(self, file_path: str):
        with open(file_path, 'r') as f:
            for line in f:
                voter, candidate = line.strip().split(',')
                self._gather_vote(voter, candidate)

    def _gather_vote(self, voter: str, candidate: str):
        if voter in self.voters:
            print(f"Fraud detected: voter {voter}")
            return

        self.voters.add(voter)
        self.candidates[candidate] = self.candidates.get(candidate, 0) + 1

    def top_three_candidates(self):
        return sorted(
            self.candidates,
            key=self.candidates.get,
            reverse=True
        )[:3]
