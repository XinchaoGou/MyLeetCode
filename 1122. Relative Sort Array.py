from typing import List
import collections
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        stat_1 = collections.Counter(arr1)
        res = []
        for i in range(len(arr2)):
            cur = arr2[i]
            cnt = stat_1[cur]
            res.extend([cur] * cnt)
            stat_1.pop(cur)
        sorted_keys = sorted(stat_1.keys())
        for k in sorted_keys:
            cnt = stat_1[k]
            res.extend([k] * cnt)
        return res


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def mycmp(x: int) -> (int, int):
            return (0, rank[x]) if x in rank else (1, x)

        rank = {x: i for i, x in enumerate(arr2)}
        arr1.sort(key=mycmp)
        return arr1