from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        right = [1]*n
        left[0], right[-1] = nums[0], nums[-1]
        for i in range(1,n):
            left[i] = left[i-1] * nums[i]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i]
        output = [0] * n
        for i in range(n):
            l = left[i-1] if i>0 else 1
            r = right[i+1] if i <n-1 else 1
            output[i] = l * r
        return output


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i]
        right = 1

        for i in range(n - 1, 0, -1):
            left[i] = left[i - 1] * right
            right *= nums[i]
        left[0] = right
        return left
