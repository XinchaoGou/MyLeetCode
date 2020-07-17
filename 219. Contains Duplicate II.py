from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        history = {}
        for i in range(len(nums)):
            v = nums[i]
            if v in history and (i - history[nums[i]] <= k):
                return True
            else:
                history[nums[i]] = i
        return False

nums = [1,2,3,1]
k = 3
print(Solution().containsNearbyDuplicate(nums, k))