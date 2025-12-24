response = {
    "results": [
        {"title": "Doc A", "text": "hello"},
        {"text": "missing title"},
        {"title": None, "text": "bad data"},
        {"title": "Horton Hears a Who", "text": "movie"}
    ]
}


def extract_titles(response: dict) -> list[str]:
    final = []
    for row in response["results"]:
        if row.get('title'):
            final.append(row)
    return final

print(extract_titles(response))