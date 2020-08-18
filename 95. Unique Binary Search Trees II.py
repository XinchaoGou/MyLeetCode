from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def geneHelper(start, end):
            if start>end:
                return [None]
            res =[]
            for i in range(start, end+1):
                left_trees = geneHelper(start, i-1)
                right_trees = geneHelper(i+1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        return geneHelper(1,n) if n else []