from typing import List

# 栈
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        left = len(nums)
        for i in range(len(nums)):
            cur = nums[i]
            while stack and cur < nums[stack[-1]]:
                left = min(left, stack.pop())
            stack.append(i)
        if left == len(nums):
            return 0

        stack = []
        right = 0
        for i in range(len(nums) - 1, -1, -1):
            cur = nums[i]
            while stack and cur > nums[stack[-1]]:
                right = max(right, stack.pop())
            stack.append(i)
        if right == 0:
            return 0
        return right - left + 1

# 优化
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        begin = 0
        end = -1
        max_val = nums[begin]
        min_val = nums[end]
        for i in range(len(nums)):
            if  nums[i] < max_val:
                end = i
            else:
                max_val = nums[i]
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > min_val:
                begin = i
            else:
                min_val = nums[i]
        return end-begin+1