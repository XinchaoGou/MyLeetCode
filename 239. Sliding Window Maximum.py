from typing import List
from collections import deque

# 双向队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        if len(nums) * k == 0:
            return []

        def clean_deq(i):
            if deq and deq[0] <= i - k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        deq = deque()
        max_idx = 0
        res = []
        for i in range(k):
            clean_deq(i)
            deq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        res.append(nums[max_idx])
        for i in range(k, len(nums)):
            clean_deq(i)
            deq.append(i)
            res.append(nums[deq[0]])
        return res


# 动态规划
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums
        if n * k == 0:
            return []

        left = [nums[0]] + [0] * (n - 1)
        right = [0] * (n - 1) + [nums[n - 1]]
        for i in range(1, n):
            # block start
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            # block end
            if (i + 1) % k == 0:
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])

        res = [max(left[i + k - 1], right[i]) for i in range(n - k + 1)]
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))