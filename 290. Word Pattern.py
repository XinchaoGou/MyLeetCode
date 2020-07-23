
class Solution:
    def wordPattern(self, pattern, str) -> bool:
        dicts = {}
        strs = str.split(" ")
        len_p = len(pattern)
        len_s = len(strs)
        if len_p != len_s:
            return False
        for i in range(len_p):
            p = pattern[i]
            if p in dicts:
                if dicts[p] != strs[i]:
                    return False
            dicts[p] = strs[i]
        return True

pattern = "abba"
str = "dog cat cat dog"
print(Solution().wordPattern(pattern, str))
