from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()
        self.__dfs(0, candidates, path, res, target)
        return res

    def __dfs(self, begin, candidates, path, res, target):
        if target == 0:
            res.append(path[:])
            return
        for i in range(begin, len(candidates)):
            if i == begin or candidates[i] != candidates[i - 1]:
                cur = candidates[i]
                residue = target - cur
                if residue < 0:
                    break
                path.append(cur)
                self.__dfs(i + 1, candidates, path, res, residue)
                path.pop()