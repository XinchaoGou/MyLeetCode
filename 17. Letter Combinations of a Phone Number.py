from typing import List
# 考虑 非法输入
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig2Str = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        res = []
        if not digits:
            return []
        if len(digits) == 1:
            if digits[0] in dig2Str:
                return dig2Str[digits[0]]
            else:
                return []
        i =0
        while not digits[i] in dig2Str:
            i += 1
        if i < len(digits):
            for c in dig2Str[digits[i]]:
                for s in self.letterCombinations(digits[i+1:]):
                    res.append(c + s)
        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig2Str = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []
        if not digits:
            return []
        if len(digits) == 1:
            return dig2Str[digits[0]]

        for c in dig2Str[digits[0]]:
            for s in self.letterCombinations(digits[1:]):
                res.append(c + s)
        return res