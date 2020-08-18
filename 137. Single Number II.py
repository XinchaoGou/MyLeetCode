from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once, twice = 0,0
        for n in nums:
            once = once ^ n & ~ twice
            twice = twice ^ n & ~ once
        return once