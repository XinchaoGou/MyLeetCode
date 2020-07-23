from typing import List

# 哈希表
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicts = {}
        res = []
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        for p in nums1:
            dicts[p] = dicts.get(p, 0) + 1
        for m in nums2:
            if m in dicts and dicts[m] > 0:
                dicts[m] -= 1
                res.append(m)
        return res

# 排序
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        res = []
        while (p1 < len(nums1) and p2 < len(nums2)):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums2[p2] < nums1[p1]:
                p2 += 1
        return res

nums1 = [1,2,2,1]
nums2 = [2,2]
print(Solution().intersect(nums1, nums2))