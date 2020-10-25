from typing import List
# 中心拓展 + 动态规划
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0
        left = [0]*len(A)
        right = [0]*len(A)
        for i in range(1, len(A)):
            if A[i]>A[i-1]:
                left[i] = left[i-1]+1
            else:
                left[i] = 0
        for i in range(len(A)-2, -1, -1):
            if A[i]>A[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 0
        res = 0
        for i in range(len(A)):
            if right[i] and left[i]:
                res = max(res, right[i] + left[i] + 1)
        return res

# 双指针
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        ans = left = 0
        while left + 2 < n:
            right = left + 1
            if A[left] < A[left + 1]:
                while right + 1 < n and A[right] < A[right + 1]:
                    right += 1
                if right < n - 1 and A[right] > A[right + 1]:
                    while right + 1 < n and A[right] > A[right + 1]:
                        right += 1
                    ans = max(ans, right - left + 1)
                else:
                    right += 1
            left = right
        return ans