import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        dicts = dict(collections.Counter(s))
        for i in range(len(s)):
            k = s[i]
            if dicts[k] == 1:
                return i
        return -1