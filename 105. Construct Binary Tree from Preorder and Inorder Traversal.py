from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildHelper(pleft, pright, inleft, inright):
            if pleft > pright:
                return None
            root = TreeNode(preorder[pleft])
            i = inleft
            while i <= inright and inorder[i] != preorder[pleft]:
                i += 1
            root.left = buildHelper(pleft+1, pleft + i -inleft, inleft, i-1)
            root.right = buildHelper(pleft+i - inleft+1, pright, i+1, inright)
            return root
        length = len(preorder)
        return buildHelper(0, length-1, 0, length-1)
