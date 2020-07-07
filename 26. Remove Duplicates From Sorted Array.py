class Solution:
    def removeDuplicates(self, nums) -> int:
        nums_len = len(nums)
        if(nums_len <= 1):
            return nums_len

        cnt = 1
        for i in range(1, len(nums)):
            if(nums[i] != nums[i-1]):
                nums[cnt] = nums[i]
                cnt += 1
        return cnt



input = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(input))

