from typing import List
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        left = 0
        right = 0
        for i in range(len(nums)):
            if nums[i] & res & (-res):
                left ^= nums[i]
            else:
                right ^= nums[i]
        return [left, right]