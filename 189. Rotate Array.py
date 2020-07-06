from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        nums_len = len(nums)
        start = 0
        i = start
        v = nums[i]
        while cnt <= nums_len - 1:
            cnt += 1
            i = (i + k) % nums_len
            t_v = nums[i]
            nums[i] = v
            if i == start:
                start += 1
                i = start
                if i <= nums_len -1:
                    v = nums[i]
                else:
                    break
                continue
            v = t_v


# ns = [1,2,3,4,5,6,7]
# k = 3
# ns = [-1,-100,3,99]
# k = 2
ns = [1]
k = 0
Solution().rotate(ns,k)
print(ns)


