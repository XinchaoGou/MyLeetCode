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
        node.left = TreeNode(m_list[i + 1])
        node.right = TreeNode(m_list[i + 2])
        layer.extend([node.left, node.right])
        i += 2
    return root

# 递归
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        r_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > r_val and q_val > r_val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p_val < r_val and q_val < r_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

# BFS
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val
        node = root
        while node:
            val = node.val
            if p_val > val and q_val > val:
                node = node.right
            elif p_val < val and q_val < val:
                node = node.left
            else:
                return node


mlist = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
# mlist = [6, 2, 8]
mTree = creat_tree(mlist)
print(Solution().lowestCommonAncestor(mTree, mTree.left.left, mTree.left.right).val)
