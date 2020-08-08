from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [False] * length
        for i in range(length-1,-1,-1):
            if (i + nums[i] >= length-1) or any(dp[i+1:i+1+nums[i]]):
                dp[i] = True
        return dp[0]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        length = len(nums)
        maxdist = nums[0]
        for i in range(length):
            if i <= maxdist:
                maxdist = max(maxdist, i + nums[i])
                if maxdist >= length-1:
                    return True
            else:
                break
        return False