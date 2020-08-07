from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        # 倒序遍历
        for i in range(length-1,-1,-1):
            # 1. 倒序第一个不是升序的数（倒着看的）
            if i-1>=0 and nums[i] > nums[i-1]:
                p = i + 1
                # 这里也可以用二分找，因为是有序的, 这里p的返回条件是小于等于要替换的数
                while (p <= length - 1 and nums[p] > nums[i-1]):
                    p += 1
                # 2. 交换， 注意这里p-1则是最后一个比目标大的数
                nums[i-1], nums[p-1] = nums[p-1], nums[i-1]

                # 3. 最后把后面的反序一下
                for k in range((length-1-i)//2 + 1):
                    nums[i+k], nums[-(1+k)] = nums[-(1+k)], nums[i+k]
                break
        # 3。 注意如果是没有找到，需要整体反序
        else:
            for k in range((length-1)//2 + 1):
                        nums[k], nums[-(1+k)] = nums[-(1+k)], nums[k]



