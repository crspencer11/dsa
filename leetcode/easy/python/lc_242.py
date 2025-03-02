class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        def hash(string):
            d = {}
            for char in string:
                if char in d:
                    d[char] += 1
                else:
                    d[char] = 1
            return d
        return hash(s) == hash(t)

