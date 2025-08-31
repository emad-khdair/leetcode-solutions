# Last updated: 8/31/2025, 4:39:00 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}

        if len(s) != len(t):
            return False

        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        return count_s == count_t