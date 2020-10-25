from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def dfs(left, right):
            if left > right or left <0 or right>len(nums)-1:
                return None
            max_idx = left
            for i in range(left, right+1, 1):
                if nums[i] > nums[max_idx]:
                    max_idx = i
            root = TreeNode(nums[max_idx])
            root.left = dfs(left, max_idx-1)
            root.right = dfs(max_idx+1, right)
            return root
        return dfs(0, len(nums)-1)

# 单调栈
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                node.left = stack.pop()

            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

nums = [3,2,1,6,0,5]
Solution().constructMaximumBinaryTree(nums)