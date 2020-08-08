from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dp = grid[-1]
        m = len(grid)
        n = len(grid[0])
        for i in range(m-1, -1,-1):
            for j in range(n-1, -1,-1):
                if i==m-1:
                    dp[j] = grid[i][j] + dp[j+1] if j <n-1 else grid[i][j]
                else:
                    dp[j] = grid[i][j] + min(dp[j+1], dp[j]) if j <n-1  else grid[i][j] + dp[j]
        return dp[0]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        dp = [float("inf")] * (n + 1)
        dp[-1] = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[j] = grid[i][j] + min(dp[j + 1], dp[j])
            dp[n] = dp[n - 1]
        return dp[0]