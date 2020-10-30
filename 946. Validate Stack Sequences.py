from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed:
            return False
        stack = []
        i, j = 0, 0
        while i < len(pushed) or j < len(popped):
            if not stack:
                stack.append(pushed[i])
                i += 1
            if stack[-1] != popped[j]:
                if i >= len(pushed): return False
                stack.append(pushed[i])
                i += 1
            else:
                if j >= len(popped): return False
                stack.pop()
                j += 1
        return True

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num) # num 入栈
            while stack and stack[-1] == popped[i]: # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack

pushed = [1,2,3,4,5]
poped = [4,5,3,2,1]
print(Solution().validateStackSequences(pushed, poped))