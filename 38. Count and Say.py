class Solution:
    def countAndSay(self, n: int) -> str:
        if(n == 1):
            return '1'

        last_str = self.countAndSay(n-1)
        v = last_str[0]
        frequent = 1
        output = ''
        for i in range(1, len(last_str)):
            if(v == last_str[i]):
                frequent += 1
            else:
                output += str(frequent) + v
                v = last_str[i]
                frequent = 1
        output += str(frequent) + v
        return output



input = 4
output = Solution().countAndSay(input)
print(output)
