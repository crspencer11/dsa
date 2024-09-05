class Solution:
    def insertionSort(self, pairs: List['Pair']) -> List[List['Pair']]:
        final = []
        for i in range(1, len(pairs)):
            current = pairs[i]
            j = i - 1
            while j >= 0 and current.key < pairs[j].key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = current
            final.append(pairs[:])
        return final

