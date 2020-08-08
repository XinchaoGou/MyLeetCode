class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dem = m + n -2
        k = n -1
        res = 1
        factor = 1
        for i in range(k):
            res *= (dem - i)
            factor *= (i+1)
        return int(res/factor)

print(Solution().uniquePaths(100,2))