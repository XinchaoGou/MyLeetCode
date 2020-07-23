# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        if not (root.left or root.right):
            return [str(root.val)]
        prefix = str(root.val) + '->'
        res = []
        if root.left:
            res = list(map(lambda x: prefix + x, self.binaryTreePaths(root.left)))
        if root.right:
            right_list = list(map(lambda x: prefix + x, self.binaryTreePaths(root.right)))
            res.extend(right_list)
        return res
