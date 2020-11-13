from typing import List
import heapq
import random


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:K])]
        heapq.heapify(q)

        n = len(points)
        for i in range(K, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            # heapq.heappushpop(q, (dist, i))
            if dist > q[0][0]:
                heapq.heapreplace(q, (dist, i))

        return [points[identity] for (_, identity) in q]


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(p):
            return p[0]**2 + p[1]**2

        def random_select(left, right, k):
            idx = random.randint(left, right)
            pivot = dist(points[idx])
            points[right], points[idx] = points[idx], points[right]
            j = left
            for i in range(left, right):
                if dist(points[i]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    j += 1
            points[right], points[j] = points[j], points[right]
            if k < j - left + 1:
                random_select(left, j-1, k)
            elif k > j - left + 1:
                random_select(j + 1, right, k - (j - left + 1))

        n = len(points)
        random_select(0, n-1, K)
        return points[:K]