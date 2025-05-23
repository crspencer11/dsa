class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited = {}
        results = []
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            if sequence in visited:
                if not visited[sequence]:
                    visited[sequence] = True
                    results.append(sequence)
            else:
                visited[sequence] = False 
        return results

