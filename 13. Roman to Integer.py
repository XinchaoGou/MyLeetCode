class Solution:
    # def romanToInt(self, s: str) -> int:
    #     R2I = {
    #         'I': 1,
    #         'V': 5,
    #         'X': 10,
    #         'L': 50,
    #         'C': 100,
    #         'D': 500,
    #         'M': 1000
    #     }
    #     result = 0
    #     i = 0
    #     while (i < len(s) - 1):
    #         current = R2I[s[i]]
    #         next = R2I[s[i + 1]]
    #         if current >= next:
    #             result += current
    #             result += next if i + 1 == len(s) - 1 else 0
    #         else:
    #             result += next - current
    #             i += 1
    #             if i + 1 == len(s) - 1:
    #                 result += R2I[s[-1]]
    #                 break
    #         i += 1
    #
    #     return result
    def romanToInt(self, s: str) -> int:
        R2I = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = R2I[s[0]]
        for i in range(1, len(s)):
            pre = R2I[s[i-1]]
            current = R2I[s[i]]
            result += current if current <= pre else current - 2*pre
        return result


s = Solution()
print(s.romanToInt("V"))
