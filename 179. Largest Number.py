# from typing import List
# import functools
# def mycmp(x,y):
#     if x+y >y+x:
#         return -1
#     if x+y < y+x:
#         return 1
#     else:
#         return 0
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         res = "".join(sorted(map(str,nums), key=functools.cmp_to_key(mycmp)))
#         return '0' if res[0] == '0' else res

# 简化
from typing import List
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x
    # def __gt__(x, y):
    #     return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = "".join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if res[0] == '0' else res



nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))
