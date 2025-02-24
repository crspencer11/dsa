class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_len = len(part)
        final = ""
        i = 0
        while i < len(s):
            final += s[i]
            i += 1
            if len(final) >= part_len:
                match = True
                for j in range(part_len):
                    if final[-part_len + j] != part[j]:
                        match = False
                        break
                if match:
                    final = final[:-part_len]
        return final

