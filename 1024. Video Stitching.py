from typing import List
# 动态规划
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [float('inf')]*(T+1)
        dp[0] = 0
        for i in range(T+1):
            for c in clips:
                if c[0] <= i <= c[1]:
                    dp[i] = min(dp[i], dp[c[0]] +1)
        return dp[T] if dp[T] < float('inf') else -1


# 贪心
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        maxn = [0] * T
        last = ret = pre = 0
        for a, b in clips:
            if a < T:
                maxn[a] = max(maxn[a], b)

        for i in range(T):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last

        return ret