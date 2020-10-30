from typing import List

# 分治递归
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def helper(start, end):
            if start >= end:
                return True
            p = start
            while postorder[p] < postorder[end]:
                p += 1
            m = p
            while postorder[p] > postorder[end]:
                p += 1
            return p == end and helper(start, m-1) and helper(m, end-1)
        return helper(0, len(postorder)-1)

# 单调栈
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True

postorder = [4, 6, 7, 5]
print(Solution().verifyPostorder(postorder))