class Solution(object):
    def getSum(self, a, b):
        MASK = 0x100000000
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b:
            answer = (a ^ b) % MASK
            carry = ((a & b) <<1) % MASK
            a,b = answer, carry
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

a = -2
b = -3
print(Solution().getSum(a,b))