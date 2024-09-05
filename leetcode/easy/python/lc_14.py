class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        smallest = min(len(first),len(last))
        for i in range(smallest):
            if first[i] != last[i]:
                return final
            final += first[i]
        return final 

