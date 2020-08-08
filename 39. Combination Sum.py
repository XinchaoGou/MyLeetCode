from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        self.__dfs(0, candidates, res, path, target)
        return res

    def __dfs(self, begin, candidates, res, path, target):
        if target == 0:
            res.append(path[:])
            return
        for i in range(begin, len(candidates)):
            residue = target - candidates[i]
            if residue < 0:
                break
            path.append(candidates[i])
            self.__dfs(i, candidates, res, path, residue)
            path.pop()