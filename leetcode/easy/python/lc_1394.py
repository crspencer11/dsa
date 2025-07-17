class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        max_lucky = -1
        for num in freq:
            if num == freq[num]:
                max_lucky = max(max_lucky, num)
        return max_lucky
