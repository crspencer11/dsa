def lengthOfLongestSubstring(s: str) -> int:
        if not s:
            return 0 
        max_length = 1
        curr = s[0]      
        for i in range(1, len(s)):
            if s[i] not in curr:
                curr += s[i]
                max_length = max(max_length, len(curr))
            else:
                index = curr.index(s[i])
                curr = curr[index + 1:] + s[i]
        return max_length
