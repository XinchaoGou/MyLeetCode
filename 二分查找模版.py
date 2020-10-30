from typing import List
# 最右
def search_right(nums: List[int], target: int) -> int:
    if not nums:
        return 0

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (right - left) // 2 + left
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            left = mid
    if nums[right] == target:
        return right
    elif nums[left] == target:
        return left
    else:
        return -1
# 最左
def search_left(nums: List[int], target: int) -> int:
    if not nums:
        return 0

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (right - left) // 2 + left
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
    else:
        return -1

nums = [8,8,8,8,8]
target = 8
print(search(nums, target))