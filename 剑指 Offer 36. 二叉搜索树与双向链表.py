"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            nonlocal head, pre
            if not cur:
                return None
            dfs(cur.left)
            if pre:
                pre.right = cur
                cur.left = pre
            else:
                head = cur
            pre = cur
            dfs(cur.right)

        if not root:
            return None
        pre = None
        head = None
        dfs(root)
        head.left = pre
        pre.right = head
        return head