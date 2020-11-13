from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        o, e = 1, 0
        res = [0] * len(A)
        for i in range(len(A)):
            if A[i] & 1:
                res[o] = A[i]
                o += 2
            else:
                res[e] = A[i]
                e += 2
        return res


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0,len(A),2):
            if A[i] & 1:
                while A[j] & 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A