class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len < 3:
            return 0
        res = 0
        curr = nums[0]
        diff = 0
        for i in range(1, nums_len):
            res = max(res, diff * nums[i])
            diff = max(diff, curr - nums[i])
            curr = max(curr, nums[i])
        return res

