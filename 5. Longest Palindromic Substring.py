class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left, right):
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return left + 1, right, right - left - 1

        start, end = 0, 0
        for i in range(len(s)):
            left1, right1, len1 = expandAroundCenter(i, i)
            left2, right2, len2 = expandAroundCenter(i, i + 1)
            if max(len1, len2) > end - start:
                if len1 > len2:
                    start, end = left1, right1
                else:
                    start, end = left2, right2
        return s[start:end]