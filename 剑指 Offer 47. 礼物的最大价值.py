from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        dp = grid[-1]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                tmp = grid[i][j]
                down = dp[j] if i+1<n else 0
                right = dp[j+1] if j+1<m else 0
                dp[j] = tmp + max(down, right)
        return dp[0]
