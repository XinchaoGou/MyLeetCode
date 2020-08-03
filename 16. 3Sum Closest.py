from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        resSum3 = float("inf")
        res = 0
        for p1 in range(length):
            p3 = length - 1
            for p2 in range(p1+1, length):
                while p2 < p3 and nums[p1] + nums[p2] + nums[p3] > target:
                    p3 -= 1
                if p2 < p3 and abs(nums[p1] + nums[p2] + nums[p3] - target) < resSum3:
                    res = nums[p1] + nums[p2] + nums[p3]
                    resSum3 = abs(res - target)
                if p3 + 1 < length and abs(nums[p1] + nums[p2] + nums[p3 + 1] - target) < resSum3:
                    res = nums[p1] + nums[p2] + nums[p3+1]
                    resSum3 = abs(res - target)
        return res

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        resSum3 = float("inf")
        res = 0
        for p1 in range(length):
            p3 = length - 1
            p2 = p1 +1
            while p2 <p3:
                sum3 = nums[p1] + nums[p2] + nums[p3]
                if sum3 == target:
                    return target
                if abs(sum3-target) < resSum3:
                    resSum3 = abs(sum3-target)
                    res = sum3
                if sum3  > target:
                    p3 -= 1
                else:
                    p2 += 1
        return res