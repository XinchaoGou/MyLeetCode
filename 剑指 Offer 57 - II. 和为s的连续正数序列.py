from typing import List
from collections import deque
# class Solution:
#     def findContinuousSequence(self, target: int) -> List[List[int]]:
#         res = []
#         stack = deque([])
#         pre_sum = 0
#         for i in range(1, target):
#             while pre_sum > target and stack:
#                 pre_sum -= stack.popleft()
#             if pre_sum == target:
#                 res.append(list(stack))
#             stack.append(i)
#             pre_sum += i
#         return res

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        l, r = 1, 2
        while l < r < target:
            sum_val = (l + r) * (r - l + 1) / 2
            if sum_val == target:
                res.append([i for i in range(l, r+1)])
                l += 1
            elif sum_val < target:
                r += 1
            else:
                l += 1
        return res

target = 9
print(Solution().findContinuousSequence(target))