class Solution:
    # 动态规划
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0]*n
        for i in range(n):
            if s[i] == ')' and i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                dp[i] = 2 + dp[i-1] + dp[i-dp[i-1] -2]
        return max(dp)

class Solution:
    # 栈
    def longestValidParentheses(self, s: str) -> int:
        length = 0
        max_length = 0
        n = len(s)
        stack = [-1]
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_length = max(max_length, length)
        return max_length

class Solution:
    # 正向逆向结合
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        left, right, max_length = 0,0,0
        # 正序遍历
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2*right)
            elif right > left:
                left = right = 0
        # 反序遍历
        left = right = 0
        for i in range(n-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2 * left)
            elif right < left:
                left = right = 0
        return max_length



input = "()(()"
print(Solution().longestValidParentheses(input))
