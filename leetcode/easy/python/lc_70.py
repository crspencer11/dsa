def climbStairs(n: int) -> int:
        return memoize(n)

def memoize(num: int, memo={}):
    if num in memo:
        return memo[num]
    if num == 0 or num == 1:
        return 1
    else:
        result = climbStairs(num-1) + climbStairs(num-2)
        memo[num] = result
        return result
