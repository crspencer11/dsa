"""
At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity").
To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.
"""
from typing import List

def knows(a, b) -> bool:
    """
    returns True if person `a` knows person `b`, else False.
    assume O(1) lookup (e.g., backed by API prolly).
    """
    pass  # implementation not provided


def find_celebrity(people: List[int]) -> int:
    """
    Returns the id of the celebrity if one exists, else -1.
    """
    n = len(people)
    if n == 0:
        return -1

    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i

    for i in range(n):
        if knows(candidate, i) or not knows(i, candidate):
            return -1
    return candidate
