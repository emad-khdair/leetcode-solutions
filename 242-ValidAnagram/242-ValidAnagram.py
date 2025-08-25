# Last updated: 8/25/2025, 9:16:50 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s , count_t = {}, {}

        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        return count_s == count_t