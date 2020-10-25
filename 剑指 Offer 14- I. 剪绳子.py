import math

# 动态规划
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(n+1):
            for j in range(i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]

# 数学
class Solution:
    def cuttingRope(self, n: int) -> int:
        a, b = divmod(n, 3)
        if n <= 3: return n-1
        if b == 0: return 3**a
        if b == 1: return 3**(a-1) * 4
        return 3**a * 2


