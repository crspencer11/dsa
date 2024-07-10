def strStr(haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        if needle_len == 0:
            return 0
        if needle_len > haystack_len:
            return -1
        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1
