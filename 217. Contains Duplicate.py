from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l1 = len(nums)
        l2 = len(set(nums))
        return not l1 == l2

input = [1,2,3]
print(Solution().containsDuplicate(input))
