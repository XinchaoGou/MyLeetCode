import heapq
import random
from typing import List


# 排序
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


# 堆
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        pq = []
        for i in range(k):
            heapq.heappush(pq, -arr[i])
        for i in range(k, len(arr), 1):
            cur = -arr[i]
            if cur > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, cur)
        return [-x for x in pq]


# 快排
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def partition(nums, l, r):
            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def randomized_partition(nums, l, r):
            i = random.randint(l, r)
            nums[i], nums[r] = nums[r], nums[i]
            return partition(nums, l, r)

        def randomized_select(arr, l, r, k):
            idx = randomized_partition(arr, l, r)
            num = idx - l + 1
            if num > k:
                r = idx - 1
                randomized_select(arr, l, r, k)
            elif num < k:
                l = idx + 1
                randomized_select(arr, l, r, k - num)

        if k == 0:
            return []
        randomized_select(arr, 0, len(arr) - 1, k)
        return arr[:k]