# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 1
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return depth
        return depth + max(self.maxDepth(root.left), self.maxDepth(root.right))


input = None
output = Solution().maxDepth(input)
print(output)
