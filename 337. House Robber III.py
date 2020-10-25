class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0,0
            lf, lg = dfs(node.left)
            rf, rg = dfs(node.right)
            return node.val + lg + rg, max(lf,lg) + max(rf, rg)
        return max(dfs(root))