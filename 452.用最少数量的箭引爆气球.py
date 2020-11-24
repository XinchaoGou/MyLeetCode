#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import List
# @lc code=start


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        pos = points[0][1]
        res = 1
        for ballon in points:
            # 找出右边界位置最靠左的气球（如果有左边界小于当前的，说明可以一起射爆
            if ballon[0] > pos: 
                pos = ballon[1]
                res += 1
        return res
# @lc code=end

