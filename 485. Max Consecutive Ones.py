from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcnt = 0
        cnt = 0
        for i in nums:
            if i:
                cnt +=1
            else:
                maxcnt = max(maxcnt,cnt)
                cnt = 0
        return max(maxcnt, cnt)