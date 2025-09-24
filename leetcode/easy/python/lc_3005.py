class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if not nums:
            return 0
        tracked = {}
        for n in nums:
            tracked[n] = tracked.get(n, 0) + 1
        max_freq = max(tracked.values())
        return sum(freq for freq in tracked.values() if freq == max_freq)

