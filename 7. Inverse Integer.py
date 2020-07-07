class Solution:
    def reverse(self, x: int) -> int:
        sig = 1 if x > 0 else -1
        x = sig*x
        result = 0
        while(x !=  0):
            rem = x % 10
            if rem != 0 or result != 0:
                result = result*10 + rem
            x = x//10
        result = result*sig
        return 0 if result > 2 ** 31 -1 or result < -2 **31 else result

s = Solution()
print(s.reverse(1534236469))

