from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def creat_tree(m_list):
    if m_list == []:
        return None
    root = TreeNode(m_list[0])
    layer = [root]
    i = 0
    while layer:
        node = layer.pop(0)
        if i >= len(m_list) - 1:
            break
        if m_list[i+1] is not None:
            node.left = TreeNode(m_list[i+1])
            layer.append(node.left)
        if m_list[i+2] is not None:
            node.right = TreeNode(m_list[i+2])
            layer.append(node.right)
        i += 2
    return root

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

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right and root.val == sum:
            return [[root.val]]

        res = []

        left = self.pathSum(root.left, sum - root.val)
        for item in left:
            res.append([root.val] + item)

        right = self.pathSum(root.right, sum - root.val)
        for item in right:
            res.append([root.val] + item)
        return res

root = creat_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
target = 22
print(Solution().pathSum(root, target))