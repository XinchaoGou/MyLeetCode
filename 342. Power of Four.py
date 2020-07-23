class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1 or num & (num -1) != 0:
            return False
        n_str = bin(num)[2:]
        cnt = 0
        for c in reversed(n_str):
            if c == '0':
                cnt += 1
            elif cnt %2 == 0:
                return True
            else:
                break
        return False