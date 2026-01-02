# Last updated: 1/2/2026, 12:02:03 PM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.min_stack = []
6
7    def push(self, val: int) -> None:
8        self.stack.append(val)
9
10        if not self.min_stack:
11            self.min_stack.append(val)
12        elif self.min_stack[-1] < val:
13            self.min_stack.append(self.min_stack[-1])
14        else:
15            self.min_stack.append(val)
16        
17
18    def pop(self) -> None:
19        self.stack.pop()
20        self.min_stack.pop()
21
22    def top(self) -> int:
23        return self.stack[-1]
24        
25
26    def getMin(self) -> int:
27        return self.min_stack[-1]
28        
29
30
31# Your MinStack object will be instantiated and called as such:
32# obj = MinStack()
33# obj.push(val)
34# obj.pop()
35# param_3 = obj.top()
36# param_4 = obj.getMin()