from typing import List

# 最高有效位
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num+1)
        i = 0
        b = 1
        while b <=num:
            while i<b and i+b<=num:
                res[i+b] = res[i]+1
                i += 1
            i = 0
            b <<= 1
        return res

# 最低有效位
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num+1)
        for i in range(num+1):
            res[i] = res[i>>1] + (i&1)
        return res

# 最后 设置位
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num+1)
        for i in range(1,num+1):
            res[i] = res[i&(i-1)] + 1
        return res