# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(l_tree: TreeNode, r_tree: TreeNode) -> bool:
            if (l_tree != None and r_tree != None) and (l_tree.val == r_tree.val):
                if (isMirror(l_tree.left, r_tree.right) and isMirror(l_tree.right, r_tree.left)):
                    return True
            return False

        if (isMirror(root.left, root.right)):
            return True
        return False


root = [1, 2, 2, 3, 4, 4, 3]
output = Solution().isSymmetric(root)
print(output)
