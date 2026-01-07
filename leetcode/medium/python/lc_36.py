from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                sq = (r // 3, c // 3)
                if sq not in squares:
                    squares[sq] = set()

                if val in rows[r] or val in cols[c] or val in squares[sq]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[sq].add(val)

        return True

