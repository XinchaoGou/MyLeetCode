# class Solution:
#     def reverse(self, x: int) -> int:
#         sig = 1 if x > 0 else -1
#         x = sig*x
#         result = 0
#         while(x !=  0):
#             rem = x % 10
#             if rem != 0 or result != 0:
#                 result = result*10 + rem
#             x = x//10
#         result = result*sig
#         return 0 if result > 2 ** 31 -1 or result < -2 **31 else result
#
# s = Solution()
# print(s.reverse(1534236469))

import collections
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        dicts = collections.Counter(nums)
        for num, cnt in enumerate(dicts):
            while dicts[num]>0:
                for j in range(k):
                    if not num + j in dicts or dicts[num + j] <1:
                        return False
                else:
                    for j in range(k):
                        dicts[num + j] -= 1
        return sum(dicts.values()) == 0

print(Solution().isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11],3))
