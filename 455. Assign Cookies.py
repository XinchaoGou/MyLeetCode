from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        for i in range(len(s)):
            if s[i] >= g[j]:
                j +=1
                if j == len(g):
                    break
        return j