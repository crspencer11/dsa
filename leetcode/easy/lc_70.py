def climbStairs(n: int) -> int:
        return self.memoize(n)

    def memoize(self, num: int, memo={}):
        if num in memo:
            return memo[num]
        if num == 0 or num == 1:
            return 1
        else:
            result = self.climbStairs(num-1) + self.climbStairs(num-2)
            memo[num] = result
            return result
