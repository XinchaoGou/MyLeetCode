from typing import List
import sys
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        minval = -sys.maxsize-1
        q = [minval, minval, nums[0]]
        for i in range(len(nums)):
            v = nums[i]
            if v == q[0] or v == q[1] or v == q[2]:
                pass
            elif v > q[2]:
                q.pop(0)
                q.append(v)
            elif v > q[1]:
                q.pop(0)
                q.insert(1, v)
            elif v > q[0]:
                q[0] = v
        return q[0] if q[0] != minval else q[2]