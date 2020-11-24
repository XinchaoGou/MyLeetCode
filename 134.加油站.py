#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from typing import List
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            v = 0
            for j in range(n):
                cur_idx = (i + j) % n
                v = v + gas[cur_idx] - cost[cur_idx]
                if v < 0:
                    break
            else:
                return i
        return -1
# @lc code=end


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            v = 0
            for j in range(n):
                cur_idx = (i + j) % n
                v = v + gas[cur_idx] - cost[cur_idx]
                if v < 0:
                    break
            else:
                return i
            i = i + j + 1
        return -1

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
# gas = [2, 3, 4]
# cost = [3, 4, 3]
print(Solution().canCompleteCircuit(gas, cost))

