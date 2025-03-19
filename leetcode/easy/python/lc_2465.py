class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 1:
            return 0
        nums.sort()
        my_set = set()
        for i in range(n // 2):
            my_set.add((nums[i] + nums[n - i - 1]) / 2)
        return len(my_set)

