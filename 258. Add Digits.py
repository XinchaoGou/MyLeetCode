class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        while (num):
            num, digits = divmod(num, 10)
            res += digits
        if res < 10:
            return res
        return self.addDigits(res)

# 官方
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return (num - 1) % 9 + 1