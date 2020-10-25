from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backTrack(i):
            nonlocal col_set, lc_set, rc_set, path, res
            for j in range(n):
                if (j in col_set) or ((i + j) in lc_set) or ((i - j) in rc_set):
                    continue
                col_set.add(j)
                lc_set.add(i + j)
                rc_set.add(i - j)
                path.append((i, j))

                if i == n-1:
                    tmp = []
                    for item in path:
                        tmp.append("."*item[1]+'Q'+'.'*(i-item[1]))
                    res.append(tmp[:])
                    # res.append(path[:])
                    # return

                backTrack(i + 1)

                path.pop()
                col_set.discard(j)
                lc_set.discard(i + j)
                rc_set.discard(i - j)

        col_set = set()
        lc_set = set()
        rc_set = set()
        res = []
        path = []
        backTrack(0)
        return res

print(Solution().solveNQueens(4))