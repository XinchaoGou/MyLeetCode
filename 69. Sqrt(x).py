class Solution:
    def mySqrt(self, x: int) -> int:
        x_cur = 1
        x_next = int(0.5*(x_cur + x/x_cur))
        while(x_next ** 2 - x > 0.5):
            x_cur = x_next
            x_next = int(0.5*(x_cur + x/x_cur))
        return x_next



input = 10
output = Solution().mySqrt(input)
print(output)
