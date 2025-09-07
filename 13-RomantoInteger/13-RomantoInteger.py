# Last updated: 9/7/2025, 5:18:37 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        i = 0
        count = 0

        while i < len(s):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                count += roman_map[s[i + 1]] - roman_map[s[i]]
                i += 2
            else:
                count += roman_map[s[i]]
                i += 1

        return count