#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
from leetcode import TreeNode, creat_tree
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def isExist(root, level, k):
            bits = 1 << (level - 1)
            node = root
            while node and bits > 0:
                if (bits & k) == 0:
                    node = node.left
                else:
                    node = node.right
                bits >>= 1
            return node is not None

        node = root
        h = -1
        while node:
            node = node.left
            h += 1

        low = 1 << h
        high = (1 << (h+1)) - 1

        while low < high:
            mid = (high - low + 1) // 2 + low
            if isExist(root, h, mid):
                low = mid
            else:
                high = mid - 1
        return low

# @lc code=end


# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         return 1 + self.countNodes(root.left) + self.countNodes(root.right)

