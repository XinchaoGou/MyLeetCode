from typing import List


class Solution:
    # my code
    # def maxSubArray(self, nums: List[int]) -> int:
    #
    #     if not nums:
    #         return -2147483648
    #
    #     sum_sub = 0
    #     left = 0
    #     right = 0
    #     sum_max = nums[0]
    #
    #     for i in range(len(nums)):
    #         v = nums[i]
    #         if (sum_sub > 0 and sum_sub + v > 0):
    #             if (left == right):
    #                 left = i
    #                 right = i + 1
    #             elif (right > left):
    #                 right += 1
    #             sum_sub += v
    #         else:
    #             left = i
    #             right = i
    #             sum_sub = v
    #         sum_max = sum_sub if sum_sub > sum_max else sum_max
    #     return sum_max

    # 动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(1,n):
            if nums[i - 1] >0:
                nums[i] += nums[i-1]
        return max(nums)

    # 贪心
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -2147483648

        cur_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum


input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# input = [-1]
input = []
output = Solution().maxSubArray(input)
print(output)
