class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     j = -1
    #     s = s.lower()
    #     for i in range(len(s) // 2):
    #         if s[i].isalnum():
    #             l = s[i]
    #             while not s[j].isalnum():
    #                 if i == len(s) + j:
    #                     break
    #                 j -= 1
    #             r = s[j]
    #             j -= 1
    #             if l != r:
    #                 return False
    #     return True

    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s.lower()))
        return s == s[::-1]


# input_str = 'A man, a plan, a canal: Panama'
# input_str = "race a car"
input_str = "Egad! Loretta has Adams as mad as a hatter. Old age!"
output = Solution().isPalindrome(input_str)
print(output)
