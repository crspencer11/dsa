class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        final = []
        for i, word in enumerate(words):
            if x in word:
                final.append(i)
        return final

