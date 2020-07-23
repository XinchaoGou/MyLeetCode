# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            g_mid = guess(mid)
            if g_mid == 0:
                return mid
            elif g_mid == 1:
                left = mid + 1
            else:
                right = mid - 1
        return 0
