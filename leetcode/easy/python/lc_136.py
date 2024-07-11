def singleNumber(nums: List[int]) -> int:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        return [j for j in dict if dict[j]==1][0]
