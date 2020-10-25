from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        idx = [0]* k
        dp = [0]* n
        dp[0] = 1
        for i in range(1, n):
            min_v = float('inf')
            for j in range(k):
                min_v = min(min_v, dp[idx[j]]*primes[j])
            dp[i] = min_v
            for j in range(k):
                if dp[i] == dp[idx[j]]*primes[j]:
                    idx[j] += 1
        return dp[n-1]