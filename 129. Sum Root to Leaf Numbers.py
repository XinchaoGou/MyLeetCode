# Definition for a binary tree node.
from collections import deque
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
        if i + 1 < len(m_list):
            node.left = TreeNode(m_list[i + 1])
            layer.append(node.left)
        if i + 2 < len(m_list):
            node.right = TreeNode(m_list[i + 2])
            layer.append(node.right)
        i += 2
    return root


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, path):
            nonlocal res
            if not node.left and not node.right:
                path.append(str(node.val))
                res += int("".join(path))
                path.pop()
                return

            if node.left:
                path.append(str(node.val))
                dfs(node.left, path)
                path.pop()

            if node.right:
                path.append(str(node.val))
                dfs(node.right, path)
                path.pop()

        res = 0
        path = []
        dfs(root, path)
        return res


# BFS
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        layer_val = deque([root.val])
        layer_node = deque([root])
        res = 0
        while layer_node:
            node = layer_node.popleft()
            val = layer_val.popleft()
            if not node.left and not node.right:
                res += val
            else:
                if node.left:
                    layer_node.append(node.left)
                    layer_val.append(10 * val + node.left.val)
                if node.right:
                    layer_node.append(node.right)
                    layer_val.append(10 * val + node.right.val)
        return res


# DFS
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, preTotal):
            if not node:
                return 0
            preTotal = preTotal * 10 + node.val
            if not node.left and not node.right:
                return preTotal
            else:
                return dfs(node.left, preTotal) + dfs(node.right, preTotal)

        return dfs(root, 0)


tree = [4, 9, 0, 5, 1]
root = creat_tree(tree)
print(Solution().sumNumbers(root))
