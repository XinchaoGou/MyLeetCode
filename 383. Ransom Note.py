class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dicts = {}
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for i in range(len(ransomNote)):
            key = ransomNote[i]
            dicts[key] = dicts.get(key, 0) + 1
        for i in range(len(magazine)):
            k = magazine[i]
            if k in dicts:
                dicts[k] -= 1

        for k, v in dicts.items():
            if v > 0:
                return False
        return True


import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

rNote = "aa"
magazine = "aab"
print(Solution().canConstruct(rNote,magazine))