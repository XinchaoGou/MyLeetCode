class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
    #     reverse = []
    #     flag = True
    #     while(x):
    #         rem = x % 10
    #         reverse.append(rem)
    #         x = x//10
    #     cnt = len(reverse)
    #     for i in range(cnt//2):
    #         if reverse[i] != reverse[cnt-1-i]:
    #             flag = False
    #             break
    #     return flag

    # def isPalindrome(self, x: int) -> bool:
    #     x_str = str(x)
    #     cnt = len(x_str)
    #     flag = True
    #     for i in range(cnt//2):
    #         if x_str[i] != x_str[cnt-1-i]:
    #             flag = False
    #             break
    #     return flag
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x%10 == 0 and x != 0)):
            return False
        reverse = 0
        while (x > reverse):
            rem = x % 10
            reverse = reverse * 10 + rem
            x = x // 10
        return x == reverse or x == reverse//10


s = Solution()
print(s.isPalindrome(10))
