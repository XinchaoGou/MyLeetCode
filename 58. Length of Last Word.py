class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for s_i in reversed(s):
            if(s_i != ' '):
                length += 1
            elif (length != 0):
                break
        return length



# input = "Hello World"
input = "a "
output = Solution().lengthOfLastWord(input)
print(output)
