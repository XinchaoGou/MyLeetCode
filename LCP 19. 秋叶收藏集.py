# 动态规划
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        f = [[0,0,0] for i in range(n)]
        f[0][0] = int(leaves[0] == 'y')
        f[0][1] = f[0][2] = f[1][2] = float('inf')

        for i in range(1, n):
            isRed = int(leaves[i] == 'r')
            isYellow = int(leaves[i] == 'y')
            f[i][0] = f[i-1][0] + isYellow
            f[i][1] = min(f[i-1][0], f[i-1][1]) + isRed
            if i >= 2:
                f[i][2] = min(f[i-1][1], f[i-1][2]) + isYellow
        return f[n-1][2]

# 前缀和 + 动态规划
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        g = (1 if leaves[0]=='y' else -1)
        gmin = g
        res = float('inf')

        for i in range(1, n):
            isYellow = int(leaves[i] == 'y')
            g += 2*isYellow -1
            if i != n-1:
                res = min(res, gmin - g)
            gmin = min(gmin, g)
        return res + (g+n)//2