import random
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
random_int = random.randint(0, 1000)

def guess(num: int) -> int:
    if num == random_int:
        return 0
    if num < random_int:
        return 1
    return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            check = guess(mid)
            if check == 0:
                return mid
            elif check == -1:
                right = mid - 1
            else:
                left = mid + 1
