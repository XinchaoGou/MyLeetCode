import itertools
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        p_list = list(itertools.permutations(s))
        history = set()
        for item in p_list:
            cur = "".join(item)
            if not cur in history:
                history.add(cur)
        return list(history)

class Solution:
    def permutation(self, s: str) -> List[str]:
        s = list(s)
        res = []

        def dfs(start):
            if start == len(s) -1:
                res.append("".join(s[:]))
                return
            history = set()
            for i in range(start, len(s)):
                if not s[i] in history:
                    history.add(s[i])
                    s[i] , s[start] = s[start], s[i]
                    dfs(start+1)
                    s[i] , s[start] = s[start], s[i]
        dfs(0)
        return res
S = "abc"
print(Solution().permutation(S))
