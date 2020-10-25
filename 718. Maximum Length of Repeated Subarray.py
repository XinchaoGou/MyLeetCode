from typing import List

# 动态规划
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        res = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] +1
                    res = max(res, dp[i][j])
        return res


# 优化空间复杂度
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)

        def maxLength(addA, addB, length):
            cnt = 0
            res = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    cnt += 1
                    res = max(res, cnt)
                else:
                    cnt = 0
            return res

        res = 0
        for i in range(m):
            length = min(n, m - i)
            res = max(res, maxLength(i, 0, length))
        for i in range(n):
            length = min(m, n - i)
            res = max(res, maxLength(0, i, length))
        return res