from typing import List
from functools import reduce
class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     return reduce(lambda x, y: x ^ y, nums)

    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                nums_set.discard(num)
            else:
                nums_set.add(num)
        return nums_set.pop()

input_list = [1,2,1]
output = Solution().singleNumber(input_list)
print(output)