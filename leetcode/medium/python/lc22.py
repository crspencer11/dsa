class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        def dfs(start, end, string):
            if start == end and start + end == n * 2:
                final.append(string)
                return
            if start < n:
                dfs(start + 1, end, string + "(")
            if end < start:
                dfs(start, end + 1, string + ")")
        dfs(0, 0, "")
        return final

