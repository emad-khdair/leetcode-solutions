# Last updated: 9/12/2025, 8:41:40 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        max_length = max(len(word1), len(word2))

        for i in range(max_length):
            if i < len(word1):
                merged.append(word1[i])

            if i < len(word2):
                merged.append(word2[i])

        return "".join(merged)
