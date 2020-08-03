class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        dicts = {}
        for i in range(len(nums2)):
            while len(stack) and nums2[i] > stack[-1]:
                dicts[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i]=dicts.get(nums1[i], -1)
        return nums1