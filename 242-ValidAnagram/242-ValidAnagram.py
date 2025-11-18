# Last updated: 11/18/2025, 8:58:34 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for char in s:
            s_map[char] = s_map.get(char, 0) + 1

        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        return s_map == t_map

        