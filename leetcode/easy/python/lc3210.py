class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        encrypted_str = ""
        n = len(s)
        for i in range(n):
            j = (i + k) % n
            encrypted_str += s[j]
        return encrypted_str

