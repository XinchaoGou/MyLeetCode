from typing import List
import collections
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 1:
            return A[0]
        counters = collections.Counter(A[0])
        for i in range(1, len(A)):
            cur_str = A[i]
            counters &= collections.Counter(cur_str)
        res = []
        for k,v in counters.items():
            res.extend([k]*v)
        return res

A = ["bella","label","roller"]
print(Solution().commonChars(A))