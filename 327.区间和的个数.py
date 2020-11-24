#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
from typing import List
# @lc code=start
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def countRangeSumRecursive(dp, left, right):
            if left == right:
                # return 1 if lower <= dp[left] <= upper else 0
                return 0
            else:
                mid = (left + right)//2
                # 使 [left, mid]有序
                n1 = countRangeSumRecursive(dp, left, mid)
                # 使 [mid+1, right]有序
                n2 = countRangeSumRecursive(dp, mid+1, right)
                res = n1 + n2

                # 首先统计下标对的数量
                i, l, r = left, mid + 1, mid + 1
                while i <= mid:
                    while l <= right and dp[l] - dp[i] <lower:
                        l += 1
                    while r <= right and dp[r] - dp[i] <= upper:
                        r += 1
                    res += (r -l)
                    i += 1
                
                # 合并两个排序数组
                dp_sorted = [0] * (right - left + 1)
                p = 0
                p1, p2 = left, mid + 1
                while p1 <= mid and p2 <= right:
                    if dp[p1] < dp[p2]:
                        dp_sorted[p] = dp[p1]
                        p1 += 1
                    else:
                        dp_sorted[p] = dp[p2]
                        p2 += 1
                    p += 1
                dp_sorted[p:] = dp[p1:mid+1] or dp[p2:]
                for i in range(len(dp_sorted)):
                    dp[left + i] = dp_sorted[i]
                return res

        dp = [0] * (len(nums)+1)
        for i in range(len(nums)):
            dp[i+1] = dp[i] + nums[i]
        
        return countRangeSumRecursive(dp, 0, len(dp)-1)
# @lc code=end


nums = [-2, 5, -1]
lower = -2
upper = 2
print(Solution().countRangeSum(nums, lower, upper))

# class Solution:
#     def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
#         if not nums:
#             return 0
#         dp = [nums[0]] * len(nums)
#         for i in range(1, len(nums)):
#             dp[i] = dp[i-1] + nums[i]
#         cnt = 0
#         for i in range(len(nums)):
#             for j in range(i+1):
#                 diff = dp[i] - dp[j-1] if j else dp[i]
#                 if lower <= diff <= upper:
#                     cnt += 1
#         return cnt


# class Solution:
#     def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
#         def countRangeSumRecursive(dp, left, right):
#             if left == right:
#                 # return 1 if lower <= dp[left] <= upper else 0
#                 return 0
#             else:
#                 mid = (left + right)//2
#                 # 使 [left, mid]有序
#                 n1 = countRangeSumRecursive(dp, left, mid)
#                 # 使 [mid+1, right]有序
#                 n2 = countRangeSumRecursive(dp, mid+1, right)
#                 res = n1 + n2

#                 # 首先统计下标对的数量
#                 i, l, r = left, mid + 1, mid + 1
#                 while i <= mid:
#                     while l <= right and dp[l] - dp[i] < lower:
#                         l += 1
#                     while r <= right and dp[r] - dp[i] <= upper:
#                         r += 1
#                     res += (r - l)
#                     i += 1

#                 # 合并两个排序数组
#                 dp_sorted = [0] * (right - left + 1)
#                 p = 0
#                 p1, p2 = left, mid + 1
#                 while p1 <= mid and p2 <= right:
#                     if dp[p1] < dp[p2]:
#                         dp_sorted[p] = dp[p1]
#                         p1 += 1
#                     else:
#                         dp_sorted[p] = dp[p2]
#                         p2 += 1
#                     p += 1
#                 dp_sorted[p:] = dp[p1:mid+1] or dp[p2:]
#                 for i in range(len(dp_sorted)):
#                     dp[left + i] = dp_sorted[i]
#                 return res

#         dp = [0] * (len(nums)+1)
#         for i in range(len(nums)):
#             dp[i+1] = dp[i] + nums[i]

#         return countRangeSumRecursive(dp, 0, len(dp)-1)
