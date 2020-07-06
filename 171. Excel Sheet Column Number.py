class Solution:
    def titleToNumber(self, s: str) -> int:
        c_len = len(s)
        if c_len < 1:
            return 0
        res = 0
        # s = s.upper()
        base = ord('A') - 1
        for c in s:
            res *= 26
            res += ord(c) - base
        return res


input = "AB"
output = Solution().titleToNumber(input)
print(output)
