from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            j = -(1 + i)
            s[i], s[j] = s[j], s[i]

class Solution:
    def reverseString(self, s):
        s.reverse()