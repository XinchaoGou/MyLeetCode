class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        vowels = set(['a', 'o','e','u','i','A','O','E','I','U'])
        s = list(s)
        while ( left < right):
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if not s[left] in vowels:
                left += 1
            if not s[right] in vowels:
                right -= 1
        return "".join(s)