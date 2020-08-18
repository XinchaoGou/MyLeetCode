from typing import List
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         length = len(nums)
#         total = 2**length
#         for i in range(total):
#             select = bin(i)[2:].zfill(length)
#             res.append([nums[j] for j in range(length) if select[j] == "1"])
#         return res
#
# # 递归
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         output = [[]]
#
#         for num in nums:
#             output += [curr + [num] for curr in output]
#
#         return output

# 回溯
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

# 二进制串
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         output = []
#
#         for i in range(2 ** n, 2 ** (n + 1)):
#             # generate bitmask, from 0..00 to 1..11
#             bitmask = bin(i)[3:]
#
#             # append subset corresponding to that bitmask
#             output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
#
#         return output

print(Solution().subsets([1,2,3]))