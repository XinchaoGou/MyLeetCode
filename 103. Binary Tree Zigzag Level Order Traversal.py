from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur_layer = [root]
        flag = False
        res = []

        while cur_layer:
            next_layer = []
            layer_val = []
            while cur_layer:
                node = cur_layer.pop(0)
                layer_val.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            if layer_val:
                if flag:
                    layer_val = layer_val[::-1]
                res.append(layer_val)
            cur_layer = next_layer
            flag = not(flag)
        return res