# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs (node):
            if not node:
                return node
            res = []
            if node.left:
                res += dfs(node.left)
            res.append(node.val)
            if node.right:
                res += dfs(node.right)
            return res
        return dfs(root)