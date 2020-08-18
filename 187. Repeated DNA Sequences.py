from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        seen, output = set(), set()

        # iterate over all sequences of length L
        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output

# 掩码
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        if n <= L:
            return []

        to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
        nums = [to_int.get(c) for c in s]

        bitmask = 0
        headmask = ~(3 << 2 * L)
        for i in range(L):
            bitmask <<= 2
            bitmask |= nums[i]
        history, output = {bitmask}, set()
        for i in range(1, n - L + 1):
            bitmask <<= 2
            bitmask |= nums[i + L - 1]
            bitmask &= headmask
            if bitmask in history:
                output.add(s[i:i + L])
            else:
                history.add(bitmask)
        return list(output)

# Rabin-Karp 算法
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        if n <= L:
            return []

        a = 4
        aL = pow(a, L)

        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]

        h = 0
        seen, output = set(), set()
        for start in range(n - L + 1):
            if start != 0:
                h = h * a - nums[start - 1] * aL + nums[start + L - 1]
            else:
                for i in range(L):
                    h = h * a + nums[i]
            if h in seen:
                output.add(s[start:start + L])
            seen.add(h)
        return output



print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))