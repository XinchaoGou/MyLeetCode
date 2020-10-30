from typing import List
class SmallNumKey(int):
    def __lt__(x,y):
        x = str(x)
        y = str(y)
        return x + y < y + x

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        sorted_nums = sorted(nums, key = SmallNumKey)
        return "".join(str(i) for i in sorted_nums)

nums = [824,938,1399,5607,6973,5703,9609,4398,8247]
print(Solution().minNumber(nums))

