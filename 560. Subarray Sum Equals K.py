from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashTable = {0:1}
        sum_val = 0
        cnt = 0
        for i in range(len(nums)):
            sum_val += nums[i]
            cnt += hashTable.get(sum_val - k, 0)
            hashTable[sum_val] = hashTable.get(sum_val, 0) + 1
        return cnt


nums = [1,1,1]
k = 2
print(Solution().subarraySum(nums, 2))




