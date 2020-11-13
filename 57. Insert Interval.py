from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = [[float('-inf'), float('-inf')]] + intervals
        n = len(intervals)
        left, right = n, n
        n_x, n_y = newInterval[0], newInterval[1]

        for i in range(n):
            if n_x < intervals[i][0]:
                left = i
                break
        for i in range(n):
            if n_y < intervals[i][0]:
                right = i
                break
        if n_x <= intervals[left - 1][1]:
            return intervals[1:left - 1] + [[min(n_x, intervals[left-1][0]) , max(intervals[right-1][1], n_y)]] + intervals[right:]
        return intervals[1:left] + [[n_x, max(n_y, intervals[right - 1][1])]] + intervals[right:]



intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
intervals = [[1,5]]
newInterval =[0,0]
print(Solution().insert(intervals, newInterval))
