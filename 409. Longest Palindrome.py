import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dicts = collections.Counter(s)
        res = 0
        single = 0
        for k,v in dicts.items():
            if v % 2 == 0:
                res += v
            else:
                if v - 1 > 0:
                    res += v-1
                single = 1
        return res + single