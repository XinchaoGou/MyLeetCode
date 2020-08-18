from typing import List
# 这个思路是往后看
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:       
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]

# 官方思路
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n+1):
            for j in range(i, -1, -1):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[-1]

#优化
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        stack = [0]
        for i in range(n+1):
            for j in range(len(stack)):
                last_true_p = stack[-(j+1)]
                if (s[last_true_p:i] in wordDict):
                    stack.append(i)
                    break
        return stack[-1] == n