class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        if len_s <1:
            return True
        s = list(s)
        t = list(t)
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
                if j == len_s:
                    return True
        return False