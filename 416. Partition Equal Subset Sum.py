from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        all_sum = sum(nums)
        if all_sum & 1 == 1:
            return False
        half_sum = all_sum // 2

        dp = [True] + [False] * half_sum

        for num in nums:
            for v in range(half_sum, num - 1, -1):
                dp[v] |= dp[v - num]
        return dp[-1]

nums = [2,2,3,5]
print(Solution().canPartition(nums))