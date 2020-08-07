from typing import List
# 利用 set 偷个懒
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        res = []
        for parenthesis in self.generateParenthesis(n-1):
            res.append("()" + parenthesis)
            for p in range(len(parenthesis)):
                res.append(parenthesis[:p] + "()" + parenthesis[p:])
        return list(set(res))

# 对 append轻微的优化
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        res = []
        history = set()
        for parenthesis in self.generateParenthesis(n-1):
            for p in range(len(parenthesis)):
                tempStr = parenthesis[:p] + "()" + parenthesis[p:]
                if not tempStr in history:
                    res.append(tempStr)
                    history.add(tempStr)
        return res

# 官方
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans