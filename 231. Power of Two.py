class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        n_str = bin(n)[2:]
        return n_str.count('1') == 1

# 官方1 x & (-x) == x
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        return n & (-n) == n

# 官方2 x & (x - 1) == 0
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0

print(Solution().isPowerOfTwo(-16))
