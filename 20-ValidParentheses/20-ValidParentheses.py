# Last updated: 11/10/2025, 7:57:34 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s_map = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in s_map.values():
                stack.append(char)
            elif stack and stack[-1] == s_map[char]:
                stack.pop()
            else:
                return False

        return not stack

        