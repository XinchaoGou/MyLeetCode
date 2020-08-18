from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def pathHelper(node, sum, path):
            if not node:
                return
            elif not (node.left or node.right) and sum == node.val:
                return res.append(path+ [node.val])
            residue = sum - node.val
            pathHelper(node.left, residue, path + [node.val])
            pathHelper(node.right, residue, path + [node.val])
        res = []
        pathHelper(root, sum, [])
        return res