#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#
from typing import List
# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def helper(left, right):
            if right <= left:
                return 0
            
            res = 0
            mid = left + (right - left)//2
            l = helper(left, mid)
            r = helper(mid+1, right)
            res = l + r

            nums[left:mid+1] = sorted(nums[left:mid+1])
            nums[mid+1:right+1] = sorted(nums[mid+1:right+1])

            j = mid+1
            for i in range(left,mid+1):
                while j <= right and nums[i] > 2*nums[j]:
                    res += mid-i+1
                    j += 1

            
            new_nums = [0] * (right - left + 1)
            p = 0
            i, j = left, mid+1
            while i<mid+1 and j< right+1:
                if nums[i] < nums[j]:
                    new_nums[p] = nums[i]
                    i += 1
                else:
                    new_nums[p] = nums[j]
                    j += 1
                p += 1
            new_nums[p:] = nums[i:mid+1] or nums[j:right+1]
            nums[left:right+1] = new_nums
            return res
        return helper(0, len(nums) - 1)
# @lc code=end

# nums = [1,3,2,3,1]
nums = [2,4,3,5,1]
print(Solution().reversePairs(nums))

