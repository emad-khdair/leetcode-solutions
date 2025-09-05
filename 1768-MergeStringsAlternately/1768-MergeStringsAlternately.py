# Last updated: 9/5/2025, 7:25:25 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        merged_string = ""

        while i < len(word1) and j < len(word2):
            merged_string += word1[i] + word2[i]
            i += 1
            j += 1

        if len(word2) > len(word1):
            merged_string += word2[j::]

        if len(word1) > len(word2):
            merged_string += word1[i::]

        return merged_string

