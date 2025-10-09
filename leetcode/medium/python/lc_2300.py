class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        for spell in spells:
            i = self.bSearch(potions, spell, success)
            if i == -1:
                pairs.append(0)
            else:
                pairs.append(len(potions) - i)
        return pairs

    def bSearch(self, potions, strength, success):
        low = 0
        high = len(potions) - 1
        i = -1
        while low <= high:
            mid = (low + high) // 2
            if potions[mid] * strength >= success:
                i = mid
                high = mid - 1
            else:
                low = mid + 1
        return i

