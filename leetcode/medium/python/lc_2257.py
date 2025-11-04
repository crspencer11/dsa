class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        guarded = set()
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2 and grid[nr][nc] != 1:
                    guarded.add((nr, nc))
                    nr += dr
                    nc += dc
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in guarded:
                    total += 1
        return total

