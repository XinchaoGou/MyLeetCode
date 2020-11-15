from typing import List
from functools import lru_cache
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         def helper(start, words):
#             w = ""
#             for i in range(start, len(s)):
#                 w += s[i]
#                 if w in wordDict:
#                     words.append(w)
#                     if i == len(s)-1:
#                         res.append(" ".join(words))
#                     helper(i+1, words)
#                     words.pop()
#
#         res = []
#         wordDict = set(wordDict)
#         helper(0, [])
#         return res

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(len(s))
        def backtrack(start):
            if start == len(s):
                return [[]]
            w = ""
            res = []
            for i in range(start, len(s)):
                w += s[i]
                if w in wordDict:
                    wordList = backtrack(i+1)
                    for wl in wordList:
                        res.append([w]+wl)
            return res


        wordDict = set(wordDict)
        res = backtrack(0)
        return [" ".join(wl) for wl in res]

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(Solution().wordBreak(s, wordDict))