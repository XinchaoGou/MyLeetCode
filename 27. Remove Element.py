class Solution:
    def removeElement(self, nums, val: int) -> int:
        tail = -1 # len>0
        nums_len = len(nums)
        for i in range(nums_len):
            if i > nums_len + tail:
                break
            if nums[i] == val:
                while(nums[tail] == val and i < nums_len+tail):
                    tail -= 1
                nums[i] = nums[tail]
                tail -= 1
        cnt = nums_len + tail + 1
        return cnt if cnt > 0 else 0


nums = []
val = 3
print(Solution().removeElement(nums, val))