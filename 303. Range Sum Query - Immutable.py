from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        length = len(nums)
        self.sums = [0] * length
        n_sums = 0
        for i in range(length):
            n_sums += self.nums[i]
            self.sums[i] = n_sums

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j] - self.sums[i - 1] if i > 0 else self.sums[j]