from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        p1 = -1
        while (left + 1 < right):
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid
        if nums[left] == target:
            p1 = left
        elif nums[right] == target:
            p1 = right
        if p1 == -1:
            return [-1, -1]

        left = p1
        right = len(nums) - 1
        while (left + 1 < right):
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] <= target:
                left = mid
        if nums[right] == target:
            p2 = right
        elif nums[left] == target:
            p2 = left

        return [p1, p2]


class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]