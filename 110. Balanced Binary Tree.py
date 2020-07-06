# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(node: TreeNode):
            if node is None:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))

        if root is None or (root.left is None and root.right is None):
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            print()
            return abs(getHeight(root.left) - getHeight(root.right)) <= 1
        return False


    # 官方
class Solution:
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        if root is None:
            return True, 0

        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, leftHeight
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, rightHeight

        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]