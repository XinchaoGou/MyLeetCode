from typing import List
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if not a:
            return []

        right = [1] * len(a)
        right[-1] = 1
        for i in range(len(a) - 2, -1, -1):
            right[i] = a[i + 1] * right[i + 1]

        # res = [0] * len(a)
        # res[0] = right[0]
        left = 1
        for i in range(1, len(a), 1):
            left *= a[i - 1]
            # res[i] = left * right[i]
            right[i] = left * right[i]
        return right