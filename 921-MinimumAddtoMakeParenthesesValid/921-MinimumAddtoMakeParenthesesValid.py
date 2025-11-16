# Last updated: 11/16/2025, 6:56:31 PM
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening_b = "("
        closing_b = ")"

        matched = 0
        unmatched = 0

        for x in s:
            if x == '(':
                unmatched += 1
            elif x == ')':
                if unmatched > 0:
                    unmatched -= 1
                else:
                    matched += 1

        return matched + unmatched