from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = left + (right - left)//2
            if (target == nums[mid]):
                left = mid
                break
            elif (target > nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return left


nums = [1, 3]
target = 2
output = Solution().searchInsert(nums, target)
print(output)
