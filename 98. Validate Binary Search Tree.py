# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True
            if not lower<node.val<upper:
                return False
            if not helper(node.left, lower, node.val):
                return False
            if not helper(node.right, node.val, upper):
                return False
            return True
        return helper(root, float("-inf"), float("inf"))


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True