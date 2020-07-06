class Solution:
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     mapping_f = {}
    #     mapping_b = {}
    #     for i in range(len(s)):
    #         if s[i] in mapping_f and mapping_f[s[i]] != t[i]:
    #             return False
    #         mapping_f[s[i]] = t[i]
    #         if t[i] in mapping_b and mapping_b[t[i]] != s[i]:
    #             return False
    #         mapping_b[t[i]] = s[i]
    #     return True
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]
            else:
                if mapping[s[i]] != t[i]:
                    return False
        return True

s = "egg"
t = "add"
print(Solution().isIsomorphic(s,t))