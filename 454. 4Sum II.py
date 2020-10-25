from typing import List
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cnt = 0
        hashtable = {}
        for a in A:
            for b in B:
                ab = a + b
                hashtable[ab] = hashtable.get(ab, 0) + 1
        for c in C:
            for d in D:
                cd = c + d
                if -cd in hashtable:
                    cnt += hashtable[-cd]
        return cnt