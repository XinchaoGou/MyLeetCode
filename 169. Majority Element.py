from typing import List
class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     length = len(nums)
    #     half_len = length//2
    #     # l_me = self.majorityElement(nums[:half_len])
    #     # r_me = self.majorityElement(nums[half_len:])
    #     num_dict = {}
    #     maj_ele = nums[0]
    #     for i in range(length):
    #         key = nums[i]
    #         num_dict[key]= num_dict.get(key, 0) + 1
    #         if num_dict[key] > half_len:
    #             maj_ele = nums[i]
    #             break
    #     return maj_ele

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate



# input = [2,2,1,1,1,2,2]
input = [6,5,5]
output = Solution().majorityElement(input)
print(output)