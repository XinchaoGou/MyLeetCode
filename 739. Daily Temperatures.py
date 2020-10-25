from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        dp = [0 for _ in range(len(T))]
        stack = [(0,len(T)-1)]
        for i in range(len(T)-1, -1, -1):
            while stack and T[i]>=stack[-1][0]:
                stack.pop()
            dp[i] = stack[-1][1] - i if stack else 0
            stack.append((T[i], i))
        return dp

T = [73,74,75,71,69,72,76,73]
T = [89,62,70,58,47,47,46,76,100,70]
print(Solution().dailyTemperatures(T))

