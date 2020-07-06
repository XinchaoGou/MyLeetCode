class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        base = ord("A") - 1
        while n > 0:
            p = n % 26
            if p:
                res += chr(p + base)
                n = n // 26
            else:
                res += chr(26 + base)
                n = n // 26 - 1
        return "".join(reversed(res))


input = 28
print(Solution().convertToTitle(input))
