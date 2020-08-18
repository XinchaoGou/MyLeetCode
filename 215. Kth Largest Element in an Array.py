import bisect
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        stack = [float("-inf")] * k
        for i in range(len(nums)):
            p = bisect.bisect_right(stack, nums[i]) - 1
            if p>=0:
                stack.pop(0)
                stack.insert(p, nums[i])
        return stack[0]

import heapq
nums = [1,8,2,23,7,-4,18,23,42,37,2]
heapq.nlargest(3,nums)
heapq.nsmallest(3,nums)

# 自带函数
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def randomPartition(a, l, r):
            i = random.randint(l, r)
            a[i], a[r] = a[r], a[i]
            return partition(a, l, r)

        def partition(a, l, r):
            x = a[r]
            i = l
            for j in range(l, r):
                if (a[j] < x):
                    a[i], a[j] = a[j], a[i]
                    i += 1
            a[i], a[r] = a[r], a[i]
            return i

        def quickSelect(nums, l, r, idx):
            q = randomPartition(nums, l, r)
            if q == idx:
                return nums[q]
            else:
                return quickSelect(nums, q + 1, r, idx) if q < idx else quickSelect(nums, l, q - 1, idx)

        return quickSelect(nums, 0, len(nums) - 1, len(nums) - k)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def maxHeapify(a, i, heapSize):
            l = i * 2 + 1
            r = i * 2 + 2
            largest = i
            if l < heapSize and a[l] > a[largest]:
                largest = l
            if r < heapSize and a[r] > a[largest]:
                largest = r
            if largest != i:
                a[i], a[largest] = a[largest], a[i]
                maxHeapify(a, largest, heapSize)

        def builMaxHeap(a, heapSize):
            for i in range(heapSize // 2, -1, -1):
                maxHeapify(a, i, heapSize)

        heapSize = len(nums)
        builMaxHeap(nums, heapSize)
        for i in range(len(nums) - 1, len(nums) - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapSize -= 1
            maxHeapify(nums, 0, heapSize)
        return nums[0]

# print(Solution().findKthLargest([-1,2,0], 2))