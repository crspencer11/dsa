class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def dfs(m: int, n: int) -> int:
            if m == 1 or n == 1:
                return 1
            if (m, n) in cache:
                return cache[(m, n)]
            cache[(m, n)] = dfs(m - 1, n) + dfs(m, n - 1)
            return cache[(m, n)]
        return dfs(m, n)

