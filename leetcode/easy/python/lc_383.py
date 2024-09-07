class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        for char in magazine:
            if char in magazine_count:
                magazine_count[char] += 1
            else:
                magazine_count[char] = 1

        for char in ransomNote:
            if char not in magazine_count or magazine_count[char] == 0:
                return False
            magazine_count[char] -= 1
        return True

