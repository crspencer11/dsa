class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums[left+1:])
        output = []
        for i in range(1, len(nums)):
            output.append(abs(left - right))
            right -= nums[i]
            left += nums[i-1]
        output.append(left)
        return output
