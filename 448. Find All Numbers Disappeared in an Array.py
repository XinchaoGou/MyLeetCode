from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            v = nums[i]
            if v != i + 1:
                while nums[v - 1] != v:
                    next_v = nums[v - 1]
                    nums[v - 1] = v
                    v = next_v
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res += [i + 1]
        return res


# 官方
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            p = abs(nums[i]) - 1
            if nums[p] > 0:
                nums[p] *= -1
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res += [i + 1]
        return res
