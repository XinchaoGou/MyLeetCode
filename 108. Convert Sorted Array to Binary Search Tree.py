from typing import List
import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        left = 0
        right = len(nums) -1
        mid = math.ceil(left + (right - left) / 2)
        root = TreeNode(nums[mid])
        if len(nums) > 1:
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root




input = [-10,-3,0,5,9]
output = Solution().sortedArrayToBST(input)
print(output)