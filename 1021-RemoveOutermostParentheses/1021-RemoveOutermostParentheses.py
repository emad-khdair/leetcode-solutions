# Last updated: 11/29/2025, 11:10:48 PM
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        result = []
4        depth = 0
5
6        for char in s:
7            if char == '(':
8                if depth > 0:
9                    result.append(char)
10                depth += 1
11            else:
12                depth -= 1
13                if depth > 0:
14                    result.append(char)
15
16        return "".join(result)