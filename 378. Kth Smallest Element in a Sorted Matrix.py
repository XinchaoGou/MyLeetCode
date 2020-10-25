from typing import List
import heapq
# 排序
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = sorted(sum(matrix,[]))
        return res[k-1]

# 最小堆维护归并排序
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        hpq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(hpq)

        for i in range(k-1):
            num, x, y = heapq.heappop(hpq)
            if y != n-1:
                heapq.heappush(hpq, (matrix[x][y+1], x, y+1))
        return heapq.heappop(hpq)[0]

# 二分法
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def check(mid):
            i, j = n-1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left<right:
            mid = (left+right)//2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left
