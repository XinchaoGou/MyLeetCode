# class Solution:
#     def convertToTitle(self, n: int) -> str:
#         res = ""
#         base = ord("A") - 1
#         while n > 0:
#             p = n % 26
#             if p:
#                 res += chr(p + base)
#                 n = n // 26
#             else:
#                 res += chr(26 + base)
#                 n = n // 26 - 1
#         return "".join(reversed(res))

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        base = ord("A") - 1
        while n:
            p = (n - 1) % 26 + 1
            res += chr(p + base)
            n = n // 26
            if p == 26 and n == 1:
                break
        return "".join(reversed(res))


input = 701
print(Solution().convertToTitle(input))
