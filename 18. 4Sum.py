from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        history = set() # 哈希表用来判断重复
        res = []
        for p1 in range(length):
            if p1< length-1 and nums[p1] + 3* nums[p1+1] > target: # 加速
                break
            if nums[p1] + 3* nums[-1] < target: # 加速
                continue
            for p2 in range(p1 + 1, length):
                # p1 和 p2 用双重循环， 剩下两个数字用双指针来找， 因为排好序了
                p3 = p2 + 1
                p4 = length - 1
                while (p3 < p4):
                    sum4 = nums[p1] + nums[p2] + nums[p3] + nums[p4]
                    if sum4 > target:
                        p4 -= 1
                    elif sum4 < target:
                        p3 += 1
                    else:
                        # 注意list可变用tuple才能放到set里
                        if not (nums[p1], nums[p2], nums[p3], nums[p4]) in history:
                            history.add((nums[p1], nums[p2], nums[p3], nums[p4]))
                            res.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                        p4 -= 1
        return res


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
