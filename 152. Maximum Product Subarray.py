from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [nums[0]] * len(nums)
        dp_min = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            num = nums[i]
            dp_max[i] = max(num, dp_max[i-1]*num, dp_min[i-1]*num)
            dp_min[i] = min(num, dp_max[i-1]*num, dp_min[i-1]*num)
        return max(dp_max)