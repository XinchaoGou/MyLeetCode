from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, cur=[]):
            if len(cur) == k:
                output.append(cur[:])
                return
            for i in range(first, n):
                if i == first or nums[i] != nums[i-1]:
                    cur.append(nums[i])
                    backtrack(i+1,cur)
                    cur.pop()
        n = len(nums)
        nums.sort()
        output = []
        for k in range(n+1):
            backtrack()
        return output

