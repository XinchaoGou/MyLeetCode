class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        res = ""
        base = ord("a") - 10
        num = num & 0xffffffff
        while num:
            p = num % 16
            num = num // 16
            res += str(p) if p < 10 else chr(p + base)
            # num = num >> 4
        return res[::-1]