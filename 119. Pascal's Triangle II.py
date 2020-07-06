from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(r_last,k):
            return int(r_last * (rowIndex - k + 1) / k)

        res = [None for _ in range(rowIndex + 1)]
        res[0] = 1
        res[-1] = 1
        for i in range(1,(rowIndex)//2 + 1):
            res[i] = helper(res[i-1], i)
            res[-(i + 1)] = res[i]
        return res


input = 5
output = Solution().getRow(input)
print(output)