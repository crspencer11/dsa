import time
import requests

BASE_URL = "https://perplexity-ai.example.com/search"

def get_with_backoff(params: dict, max_retries: int = 3) -> dict:
    for attempt in range(max_retries + 1):
        response = requests.get(BASE_URL, params=params, timeout=5)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 429:
            if attempt == max_retries:
                raise RuntimeError("Rate limit exceeded")
            time.sleep(2 ** attempt)
            continue

        if response.status_code == 500:
            raise RuntimeError("Server error")

        response.raise_for_status()

    raise RuntimeError("Unreachable")

def fetch_all_results(query: str) -> list[dict]:
    results = []
    page = 1

    while True:
        data = get_with_backoff({"q": query, "page": page})
        results.extend(data.get("results", []))

        if not data.get("has_more"):
            break

        page += 1

    return results

data = {
  "results": [
    {"id": "1", "text": "...", "score": 0.92},
    {"id": "2", "text": "...", "score": 0.87}
  ],
}
