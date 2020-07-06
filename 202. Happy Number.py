class Solution:
    def isHappy(self, n: int) -> bool:
        happyFlag = False
        history = set()
        while(not n in history):
            history.add(n)
            res = 0
            while (n):
                n, digit = divmod(n, 10)
                res += digit ** 2
            if res == 1:
                happyFlag = True
                break
            n = res
        return happyFlag





input = 10
print(Solution().isHappy(input))