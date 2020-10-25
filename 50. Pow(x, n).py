# 递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(x, n):
            if n==0 or x ==1:
                return 1
            y = quickMul(x, n>>1)
            return y*y*x if n&1 else y*y
        return quickMul(x, n) if n>0 else 1.0/quickMul(x, -n)

# 迭代
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x== 0:
            return 0
        if x == 1 or n == 0:
            return 1
        ans = 1
        res = x
        abs_n = abs(n)
        while abs_n:
            if abs_n&1:
                ans *= res
            res *= res
            abs_n = abs_n >> 1
        return ans if n > 0 else 1.0/ans