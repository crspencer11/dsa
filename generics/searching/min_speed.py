import numpy as np
"""
You’re given an array piles[p] (up to 1e9 each), and a hours[h] (up to 1e12)

You can choose an integer speed k

Each hour, you process k items from a single pile
If a pile has less than k, you finish it in that hour

Return the minimum k such that all piles are finished within h
"""

def min_speed(piles: list[np.uint32], hours: np.uint64) -> int:
    left, right = 1, max(piles)

    def can_finish(k: np.uint32) -> bool:
        total = 0
        for pile in piles:
            total += (pile + k - 1) // k
            if total > hours:  # early term gets the worm
                return False
        return total <= hours

    while left < right:
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1

    return left


