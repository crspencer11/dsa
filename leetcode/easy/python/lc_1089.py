class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        def findZeros():
            total = 0
            for num in arr:
                if num == 0:
                    total += 1
            return total
        n = len(arr)
        zeros = findZeros()
        i = n - 1
        j = n + zeros - 1
        while i >= 0:
            if j < n:
                arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -= 1
            i -= 1

