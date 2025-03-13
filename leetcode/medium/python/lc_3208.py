class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int: 
        n = len(colors)
        count = 0
        i = 0
        for j in range(n + k - 1):
            if j > 0 and colors[j % n] == colors[(j - 1) % n]:
                i = j  
            if j - i + 1 >= k:
                count += 1  
        return count

