class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def helper(node):
            if not node:
                return []
            return helper(node.left) + [node.val] + helper(node.right)
        return  helper(root)[k-1]

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = [root]
        while stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        return -1

