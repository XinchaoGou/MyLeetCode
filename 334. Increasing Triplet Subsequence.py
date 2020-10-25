from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = float('inf')
        mid = float('inf')
        for i in range(len(nums)):
            v = nums[i]
            if v <= small:
                small = v
            elif v <= mid:
                mid = v
            elif v > mid:
                return True
        return False