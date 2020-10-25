# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            nonlocal total
            if node:
                dfs(node.right)
                total += node.val
                node.val = total
                dfs(node.left)

        total = 0
        dfs(root)
        return root