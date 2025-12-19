class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        threshold = n / 2
        my_map = {nums[0]: 1}
        for i in range(1, n):
            if nums[i] in my_map:
                my_map[nums[i]] += 1
                if my_map[nums[i]] >= threshold:
                    return nums[i]
            else:
                my_map[nums[i]] = 1
        return 0
