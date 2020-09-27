from typing import List

# 二分法
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        right = n-1
        while left <= right:
            mid = (left + right)//2
            cnt = 0
            for i in range(n):
                if nums[i] <= mid:
                    cnt +=1
            if cnt <= mid:
                left = mid+1
            else:
                right = mid-1
        return left

# Floyd 判圈算法
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]
        return nums[slow]

nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums))

