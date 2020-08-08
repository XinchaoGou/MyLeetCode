from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        m = len(matrix)
        n = len(matrix[0])
        num = m * n
        cnt = 0
        top = 0
        left = 0
        right = n -1
        bottom = m -1
        while cnt < num:
            for j in range(left, right+1):
                res.append(matrix[top][j])
                cnt += 1
            top += 1
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
                cnt += 1
            right -= 1
            if (cnt < num):
                for j in range(right, left-1, -1):
                    res.append(matrix[bottom][j])
                    cnt += 1
                bottom -= 1
                for i in range(bottom, top-1,-1):
                    res.append(matrix[i][left])
                    cnt += 1
                left += 1
        return res

print(Solution().spiralOrder([[1,2],[5,6]]))
