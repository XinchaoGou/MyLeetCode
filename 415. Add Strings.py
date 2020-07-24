class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        len1 = len(num1)
        len2 = len(num2)
        length = max(len1, len2)
        c = 0
        res = ""
        i = 1
        while i <= length:
            v = c
            if i <= len1:
                v += int(num1[-i])
            if i <= len2:
                v += int(num2[-i])
            if v >= 10:
                c = 1
                v %= 10
            else:
                c = 0
            res += str(v)
            i += 1
        if c:
            res += "1"
        return "".join(reversed(res))

num1 = "123"
num2 = "27"
print(Solution().addStrings(num1, num2))