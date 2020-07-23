from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        cnt = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
            else:
                cnt += 1
        for i in range(length - cnt, length, 1):
            nums[i] = 0

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)
