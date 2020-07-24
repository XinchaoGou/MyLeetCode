# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        layer = [root]
        res = 0
        while layer:
            node = layer.pop(0)
            left = node.left
            right = node.right
            if left:
                layer.append(left)
                if not any([left.left, left.right]):
                    res += left.val
            if right:
                layer.append(right)
        return res