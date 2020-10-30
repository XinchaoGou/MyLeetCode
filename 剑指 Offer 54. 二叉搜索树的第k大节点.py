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
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stack = [root]
        while stack:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.left
        return 0