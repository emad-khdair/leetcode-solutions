# Last updated: 11/12/2025, 10:02:18 AM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0

        for char in s:
            if char == '(':
                if depth > 0:
                    result.append(char)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result.append(char)

        return "".join(result)