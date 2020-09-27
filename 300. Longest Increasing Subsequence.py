from typing import List


# 动态规划
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

# 贪心 + 二分
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for i in range(len(nums)):
            cur = nums[i]
            if not d or cur > d[-1]:
                d.append(cur)
            else:
                l = 0
                r = len(d) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= cur:
                        r = mid - 1
                    else:
                        l = mid + 1
                d[l] = cur
        return len(d)


nums = [10,9,2,5,3,4]
# nums = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
print(Solution().lengthOfLIS(nums))
