from typing import List


class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     def search_helper(l, t: int):
    #         r = len(numbers) - 1
    #         while (l <= r):
    #             mid = int(l + (r - l) / 2)
    #             mid_val = numbers[mid]
    #             if mid_val == t:
    #                 return mid
    #             elif mid_val > t:
    #                 r = mid - 1
    #             else:
    #                 l = mid + 1
    #         return None
    #
    #     res = []
    #     for i in range(len(numbers)):
    #         t = target - numbers[i]
    #         if (t >= numbers[i]):
    #             searched = search_helper(i+1, t)
    #             if searched:
    #                 res = [i + 1, searched + 1]
    #                 break
    #         else:
    #             break
    #     return res
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while(l < r):
            sum_val = numbers[l] + numbers[r]
            if sum_val == target:
                return [l+1, r+1]
            elif sum_val > target:
                r -= 1
            else:
                l +=1
        return []


numbers = [1,2,3,4,4,9,56,90]
target = 8
output = Solution().twoSum(numbers, target)
print(output)
