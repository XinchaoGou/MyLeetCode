import math

# 动态规划
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(int(math.sqrt(n)) + 1)]
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1, n + 1):
            for s_num in square_nums:
                if i < s_num:
                    break
                dp[i] = min(dp[i], dp[i-s_num] + 1)
        return dp[-1]

# 贪心枚举
class Solution:
    def numSquares(self, n: int) -> int:
        def isDividedBy(n, count):
            if count == 1:
                return n in square_nums
            for k in square_nums:
                if isDividedBy(n- k, count - 1):
                    return True
            return False
        square_nums = set(i**2 for i in range(int(math.sqrt(n))+1))
        for i in range(1, n+1):
            if isDividedBy(n, i):
                return i

# 贪心 + BFS
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        level = 0
        queue = {n}
        while queue:
            level += 1
            next_queue = set()
            for remainder in queue:
                for s_num in square_nums:
                    if remainder == s_num:
                        return level
                    elif remainder < s_num:
                        break
                    else:
                        next_queue.add(remainder - s_num)
            queue = next_queue
        return level

# 数学运算
class Solution:
    def isSquare(self, n: int) -> bool:
        sq = int(math.sqrt(n))
        return sq*sq == n

    def numSquares(self, n: int) -> int:
        # four-square and three-square theorems
        while (n & 3) == 0:
            n >>= 2      # reducing the 4^k factor from number
        if (n & 7) == 7: # mod 8
            return 4

        if self.isSquare(n):
            return 1
        # check if the number can be decomposed into sum of two squares
        for i in range(1, int(n**(0.5)) + 1):
            if self.isSquare(n - i*i):
                return 2
        # bottom case from the three-square theorem
        return 3