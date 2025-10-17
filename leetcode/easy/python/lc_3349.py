class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        count = 1
        increasing_segments = []
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                if count >= k:
                    increasing_segments.append(count)
                count = 1
        if count >= k:
            increasing_segments.append(count)
        return len(increasing_segments) >= 2

