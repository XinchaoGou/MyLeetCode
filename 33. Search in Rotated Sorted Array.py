from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while (left + 1 < right):
            mid = left + (right - left) // 2
            if nums[mid] > nums[0]:
                left = mid
            elif nums[mid] < nums[0]:
                right = mid

        if target < nums[0]:
            right = len(nums) - 1
        elif target > nums[0]:
            left = 0
        else:
            return 0

        while (left + 1 < right):
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

#  官方 优化
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while (left+1<right):
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]:
                if nums[mid] > target >= nums[0]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

print(Solution().search([5,1,3], 5))
