class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        highest = second = third = float('-inf')
        lowest = second_lowest = float('inf')
        for num in nums:
            if num > highest:
                third = second
                second = highest
                highest = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
            if num < lowest:
                second_lowest = lowest
                lowest = num
            elif num < second_lowest:
                second_lowest = num

        return max(highest * second * third, highest * lowest * second_lowest)

