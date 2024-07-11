def twoSum(nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i, val in enumerate(nums):
            remainder = target - val
            if remainder in tracker:
                return [i, tracker[remainder]]
            tracker[val] = i
