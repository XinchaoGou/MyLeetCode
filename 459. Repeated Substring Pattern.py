class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]

# 利用KMP
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        next = [-1] * n
        for i in range(1,n):
            j = next[i-1]
            while j >= 0 and s[j+1] != s[i]:
                j = next[j]
            if s[j+1] == s[i]:
                next[i] = j + 1
        return next[-1] >= 0 and n % (n - 1 - next[-1]) == 0
