from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    #     binary_tree = []
    #     if root is None:
    #         return binary_tree
    #
    #     layer = []
    #     layer.append(root)
    #     binary_tree.append(layer)
    #     while layer != []:
    #         sub_layer = []
    #         for node in layer:
    #             if node.left != None:
    #                 sub_layer.append(node.left)
    #             if node.right != None:
    #                 sub_layer.append(node.right)
    #         layer = sub_layer
    #         if layer != []:
    #             binary_tree.append(layer)
    #
    #     results = []
    #     for layer in reversed(binary_tree):
    #         result_layer = [node.val for node in layer]
    #         results.append(result_layer)
    #     return results

    # 官方

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        binary_tree = []
        if root is None:
            return binary_tree

        layer = []
        layer_val = []
        layer.append(root)
        layer_val.append(root.val)
        binary_tree.append(layer_val)
        while layer != []:
            sub_layer = []
            layer_val = []
            for node in layer:
                if node.left != None:
                    sub_layer.append(node.left)
                    layer_val.append(node.left.val)
                if node.right != None:
                    sub_layer.append(node.right)
                    layer_val.append(node.right.val)
            layer = sub_layer
            if layer != []:
                binary_tree.append(layer_val)

        return reversed(binary_tree)

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue =[]
        cur = [root]

        while cur:
            cur_layer_val = []
            next_layer_node = []
            for node in cur:
                if node:
                    cur_layer_val.append(node.val)
                    next_layer_node.extend([node.left, node.right])
            if cur_layer_val:
                queue.insert(0, cur_layer_val)
            cur = next_layer_node
        return queue






input = None
output = Solution.levelOrderBottom(input)
print(output)
