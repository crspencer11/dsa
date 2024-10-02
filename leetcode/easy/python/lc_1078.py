class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        split = text.split()
        final = []
        for i in range(len(split) - 2):
            if split[i] == first and split[i+1] == second:
                final.append(split[i+2])
        return final

