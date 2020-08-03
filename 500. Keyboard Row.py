from typing import List
# 该方法最快
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set_1 = set("QWERTYUIOP")
        set_2 = set("ASDFGHJKL")
        set_3 = set("ZXCVBNM")
        res = []
        for word in words:
            word_set = set(word.upper())
            if not (word_set - set_1) or not (word_set - set_2) or not (word_set - set_3):
                res.append(word)
        return res

# 利用 issubset
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set_1 = set("QWERTYUIOP")
        set_2 = set("ASDFGHJKL")
        set_3 = set("ZXCVBNM")
        res = []
        for word in words:
            word_set = set(word.upper())
            if word_set.issubset(set_1) or word_set.issubset(set_2) or word_set.issubset(set_3):
                res.append(word)
        return res

# 求交集
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set_1 = set("QWERTYUIOP")
        set_2 = set("ASDFGHJKL")
        set_3 = set("ZXCVBNM")
        res = []
        for word in words:
            word_set = set(word.upper())
            if word_set&set_1== word_set or word_set&set_2== word_set or word_set&set_3== word_set:
                res.append(word)
        return res