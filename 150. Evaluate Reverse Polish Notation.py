from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in ["+","-","*","/"]:
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()
                if c == "+":
                    stack.append(a+b)
                if c == "-":
                    stack.append(a-b)
                if c == "*":
                    stack.append(a*b)
                if c == "/":
                    stack.append(int(a/b))
        return stack[-1]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(c)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(str(int(eval(a + c + b))))
        return int(stack[-1])

print(Solution().evalRPN(["4","13","5","/","+"]))