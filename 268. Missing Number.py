from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n_set = set(nums)
        for i in range(len(nums)):
            if not i in n_set:
                return i
        return len(nums)