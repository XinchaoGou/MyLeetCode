from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur_layer = [root]
        res = []

        while cur_layer: #判断是否该层为空
            next_layer = []
            layer_val = []
            while cur_layer: #遍历该层所有节点
                node = cur_layer.pop(0)
                layer_val.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            if layer_val:
                res.append(layer_val)
            cur_layer = next_layer
        return res