class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        final = []
        maximum = max(arr)
        i = 0
        for i in range(len(arr) - 1):
            if arr[i] != maximum:
                final.append(maximum)
            else:
                maximum = max(arr[i + 1:])
                final.append(maximum)
        final.append(-1)
        return final


