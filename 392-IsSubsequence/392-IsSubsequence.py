# Last updated: 9/5/2025, 8:52:31 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        if len(t) == 0:
            return False

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else: 
                j += 1

        return i == len(s)