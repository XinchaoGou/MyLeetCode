class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while k and stack and num[i] < stack[-1]:
                stack.pop()
                k -=1
            stack.append(num[i])
        finalstack = stack[:-k] if k else stack
        return "".join(finalstack).lstrip('0') or '0'