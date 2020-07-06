# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         result = int(a, 2) + int(b, 2)
#         return bin(result)[2:]

class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
a = "11"
b = "1"
output = Solution().addBinary(a, b)
print(output)
