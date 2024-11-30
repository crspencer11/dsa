class Solution:
    def fib(self, n: int) -> int:
        cache = {}

        def helper(n):
            if n in cache:
                return cache[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            result = helper(n - 1) + helper(n - 2)
            cache[n] = result
            return result
        return helper(n)

