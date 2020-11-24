#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#
from typing import List

# @lc code=start
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        max_length = max(r0, R-1-r0) + max(c0, C-1-c0)
        res = [[r0, c0]]
        for l in range(1, max_length+1):
            r = r0 - l
            c = c0
            for d in range(len(dirs)):
                dr, dc = dirs[d]
                for i in range(l):
                    if 0 <= r < R and 0 <= c < C:
                        res.append([r, c])
                    r += dr
                    c += dc
        return res
        

# @lc code=end

# 方法一排序
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        Rec = [(i, j) for j in range(C) for i in range(R)]
        Rec.sort(key=lambda x: abs(x[0]-r0) + abs(x[1]-c0))
        return Rec
# 方法二 桶排序
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def dist(i, j):
            return abs(i-r0) + abs(j - c0)
        max_dist = max(r0, R-1-r0) + max(c0, C-1-c0)
        stat = collections.defaultdict(list)
        for i in range(R):
            for j in range(C):
                stat[dist(i, j)].append([i, j])
        res = []
        for i in range(max_dist+1):
            res.extend(stat[i])
        return res
# 方法三 几何
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        max_length = max(r0, R-1-r0) + max(c0, C-1-c0)
        res = [[r0, c0]]
        for l in range(1, max_length+1):
            r = r0 - l
            c = c0
            for d in range(len(dirs)):
                dr, dc = dirs[d]
                for i in range(l):
                    if 0 <= r < R and 0 <= c < C:
                        res.append([r, c])
                    r += dr
                    c += dc
        return res

# R = 1
# C = 2
# r0 = 0
# c0 = 0
R = 4
C = 7
r0 = 3
c0 = 2
print(Solution().allCellsDistOrder(R, C, r0, c0))
