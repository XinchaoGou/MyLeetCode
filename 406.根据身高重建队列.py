#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
# [7,0], [7,1], [6,1], [5,0], [5,2], [4,4]
# 再一个一个插入。
# [7,0]
# [7,0], [7,1]
# [7,0], [6,1], [7,1]
# [5,0], [7,0], [6,1], [7,1]
# [5,0], [7,0], [5,2], [6,1], [7,1]
# [5,0], [7,0], [5,2], [6,1], [4,4], [7,1]

from typing import List
# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            spaces = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans
# @lc code=end

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(Solution().reconstructQueue(people))