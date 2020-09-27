from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp_u = [0] * n
        dp_l = [0] * n
        dp_r = [n] * n
        res = 0
        cur_left, cur_right = 0, n-1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    dp_u[j] = 0
                    dp_l[j] = 0
                    cur_left = j + 1
                else:
                    dp_u[j] += 1
                    dp_l[j] = max(cur_left, dp_l[j])
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "0":
                    dp_r[j] = n
                    cur_right = j
                else:
                    dp_r[j] = min(cur_right, dp_r[j])
                    res = max(res, dp_u[j] * (dp_r[j] - dp_l[j]))
        return res


class Solution:
    # Get the maximum area in a histogram given its heights
    def leetcode84(self, heights):
        stack = [-1]
        maxarea = 0
        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return maxarea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            maxarea = max(maxarea, self.leetcode84(dp))
        return maxarea

rec = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalRectangle(rec))