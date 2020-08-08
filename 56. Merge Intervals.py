from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            last = res[-1]
            x= sorted_intervals[i]
            if x[0]<=last[1]:
                res[-1][1] = max(last[1],x[1])
            else:
                res.append(x)
        return res