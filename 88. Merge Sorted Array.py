from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while(p1 >= 0  and p2 >= 0):
            if(nums1[p1] >= nums2[p2]):
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2+1] = nums2[:p2+1]

    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     p1 = m - 1
    #     p2 = n - 1
    #     for i in range(m + n - 1, -1, -1):
    #         if(p1 < 0):
    #             nums1[i] = nums2[p2]
    #             p2 -= 1
    #             continue
    #         if(p2 < 0):
    #             p1 -= 1
    #             continue
    #         if (nums1[p1] >= nums2[p2]):
    #             nums1[i] = nums1[p1]
    #             p1 -= 1
    #         else:
    #             nums1[i] = nums2[p2]
    #             p2 -= 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

Solution().merge(nums1, 3, nums2, 3)
print(nums1)
