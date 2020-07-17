# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        layer = [root]
        while(layer):
            node = layer.pop()
            left = node.left
            right = node.right
            node.right = left
            node.left = right
            if left:
                layer.append(left)
            if right:
                layer.append(right)
        return root