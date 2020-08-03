from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length):
            if i == 0 or nums[i] != nums[i-1]:
                target = -nums[i]
                third = length-1
                for j in range(i+1,length):
                    if j == i+1 or nums[j] != nums[j -1]:
                        while j<third and nums[j] + nums[third] > target:
                            third -= 1
                        if j<third and nums[j] + nums[third] == target:
                            res.append([nums[i], nums[j], nums[third]])
        return res

