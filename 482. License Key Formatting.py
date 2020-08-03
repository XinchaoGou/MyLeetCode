class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res = ""
        s_t = ""
        for c in reversed(S):
            if c.isalnum():
                c = c.upper()
                if len(s_t) < K:
                    s_t = c + s_t
                else:
                    res = s_t + "-" + res if res else s_t
                    s_t = c
        return s_t +"-"+res if res else s_t

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = list("".join(filter(str.isalnum, S.upper())))
        for i in range(len(s) - K, 0, -K):
            s.insert(i, "-")
        return "".join(s)