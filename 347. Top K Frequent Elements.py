import collections
from typing import List


# 自带函数
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stat = collections.Counter(nums)
        return [t[0] for t in stat.most_common(k)]


# 堆
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def sift_down(arr, root, k):
            l = root << 1
            r = l | 1
            while l < k:
                child = l
                if r < k and arr[r][1] < arr[l][1]:
                    child = r
                if arr[child][1] < arr[root][1]:
                    arr[child], arr[root] = arr[root], arr[child]
                    root = child
                    l = child << 1
                    r = l | 1
                else:
                    break
            return

        def sift_up(arr, child):
            father = child >> 1
            while father > 0 and arr[child][1] < arr[father][1]:
                arr[child], arr[father] = arr[father], arr[child]
                child >>= 1
                father >>= 1

        stat = list(collections.Counter(nums).items())
        heap = [(0, 0)]
        for i in range(k):
            heap.append(stat[i])
            sift_up(heap, i + 1)
        for i in range(k, len(stat)):
            if stat[i][1] > heap[1][1]:
                heap[1] = stat[i]
                sift_down(heap, 1, k + 1)
        return [item[0] for item in heap[1:]]


# 快速排序
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def partition(arr, l, r):
            i = l
            pivot = r
            for j in range(l, r):
                if arr[j][1] >= arr[pivot][1]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[pivot], arr[i] = arr[i], arr[pivot]
            return i

        def qsort(arr, l, r, k):
            while l <= r:
                pivot = partition(arr, l, r)
                if pivot == k - 1:
                    return [item[0] for item in arr[:k]]
                elif pivot < k - 1:
                    l = pivot + 1
                else:
                    r = pivot - 1

        stat = list(collections.Counter(nums).items())
        return qsort(stat, 0, len(stat) - 1, k)


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = collections.Counter(nums)
#         val = list(counter.keys())
#         l, r = 0, len(val) - 1
#         while l <= r:
#             pivot = self.partition(val, l, r, counter)
#             if pivot == k - 1:
#                 return val[:k]
#             if pivot > k - 1:
#                 r = pivot - 1
#             else:
#                 l = pivot + 1
#
#     def partition(self, val, l, r, counter):
#         ran = random.randint(l, r)
#         val[ran], val[r] = val[r], val[ran]
#         pivot = r
#         right = l
#         for i in range(l, r):
#             if counter.get(val[i]) >= counter.get(val[pivot]):
#                 val[i], val[right] = val[right], val[i]
#                 right += 1
#         val[right], val[pivot] = val[pivot], val[right]
#         return right

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         def sift_down(arr, root, k):
#             """下沉log(k),如果新的根节点>子节点就一直下沉"""
#             val = arr[root] # 用类似插入排序的赋值交换
#             while root<<1 < k:
#                 child = root << 1
#                 # 选取左右孩子中小的与父节点交换
#                 if child|1 < k and arr[child|1][1] < arr[child][1]:
#                     child |= 1
#                 # 如果子节点<新节点,交换,如果已经有序break
#                 if arr[child][1] < val[1]:
#                     arr[root] = arr[child]
#                     root = child
#                 else:
#                     break
#             arr[root] = val
#
#         def sift_up(arr, child):
#             """上浮log(k),如果新加入的节点<父节点就一直上浮"""
#             val = arr[child]
#             while child>>1 > 0 and val[1] < arr[child>>1][1]:
#                 arr[child] = arr[child>>1]
#                 child >>= 1
#             arr[child] = val
#
#         stat = collections.Counter(nums)
#         stat = list(stat.items())
#         heap = [(0,0)]
#
#         # 构建规模为k+1的堆,新元素加入堆尾,上浮
#         for i in range(k):
#             heap.append(stat[i])
#             sift_up(heap, len(heap)-1)
#         # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
#         for i in range(k, len(stat)):
#             if stat[i][1] > heap[1][1]:
#                 heap[1] = stat[i]
#                 sift_down(heap, 1, k+1)
#         return [item[0] for item in heap[1:]]

# nums = [1,1,1,2,2,3]
# nums = [1,1,1,2,2,3,3,3,3,3,4,4,4,4,5,4,3]
# nums = [4,1,-1,2,-1,2,3]
nums = [-5, -9, 67, -10, 4, -57, 47, 13, -67, -26, -57, 63, 38, -68, 62, -45, -37, 95, 49, -91, -53, -42, -33, 80, 78,
        -30, -36, 22, 9, -86, 79, -1, 44, -92, 30, -68, -94, 58, -51, -26, -38, 5, -74, 25, 71, -93, 52, -12, -86, 7,
        -86, 53, 78, -31, -5, -87, 88, -98, -39, 9, 99, 23, 96, -90, 51, -64, 35, -73, 9, 60, -78, 70, 99, 14, 70, 71,
        -78, 50, 7, 46, -89, 57, -1, 87, -87, -95, 48, 49, 79, -54, 31, 28, -27, 75, 31, -76, -12, 35, 40, -90, -60,
        -60, -7, 67, 73, -34, -42, -35, 61, 51, 18, 95, 16, 78, -81, -91, -30, 92, 57, -79, 5, 41, 29, 72, -62, -47, 80,
        29, 1, -21, -36, 5, 82, 4, -12, -52, -56, -47, -68, 95, 85, -87, -7, -12, 98, 75, -64, -93, 11, 73, -81, -9,
        -12, -9, 51, 17, -94, 33, -9, 57, -35, 10, -17, 87, -18, -55, -52, 30, -62, 73, 35, -74, -47, -63, 77, -72, -55,
        5, 73, 21, 14, 7, -65, -51, -55, -49, 98, -20, -22, -68, 34, -20, 92, 55, 47, -20, 6, -54, -12, 3, 75, 69, 60,
        15, 88, 64, 2, -27, -50, 55, 73, 46, -15, -64, 93, -47, -75, -55, -75, 21, -57, 91, -12, -99, -68, -56, -14, -4,
        -77, -94, 55, 93, -31, 68, -12, -23, 59, -56, -86, 43, 83, -93, -78, -11, -7, 96, -3, -87, -37, 19, -78, 67,
        -29, 77, -28, 91, -73, -68, -22, 18, -7, 3, 15, 77, 99, 31, -48, -86, -45, -82, 52, -39, 8, -88, -83, -58, -77,
        5, 87, -61, 50, 32, -66, -36, 60, -53, 52, 70, -36, -1, 83, -56, 33, 98, -80, 28, 1, -21, -50, -60, 44, 99, 18,
        83, -29, 83, -36, -55, -6, 96, -60, 61, 75, 6, -57, 2, 82, 62, -27, 36, 60, 72, 92, 61, -65, 79, -57, -34, -23,
        -28, -55, 53, 36, -80, 5, -76, 64, -81, -32, -43, -1, 50, -16, -72, -74, 22, 88, 28, -79, -99, 85, -13, -34,
        -76, 85, 6, 21, -99, 10, -46, 79, 11, -70, 17, 47, -22, -62, 0, 6, 75, -19, 57, -25, -52, -83, 90, 21, 95, 52,
        68, 47, -12, 76, -9, -65, 86, 90, 16, 74, 64, 26, 84, 64, -42, 97, -72, 53, -76, 11, 89, -62, 67, 100, 15, 53,
        68, -16, 24, 11, -77, 20, 59, -95, -50, -20, 27, 45, 94, 13, -93, 86, 49, 12, 19, 17, -33, -52, -28, 71, 79,
        -19, -73, 40, -99, 83, 77, 19, -20, 98, 86, -5, -5, 73, 18, 100, 73, -45, 33, 3, 89, 32, -53, 73, 16, -3, -26,
        -80, 49, -78, 67, 31, 1, -85, -44, -91, -68, 75, -74, 95, 23, 89, 99, -84, 54, -93, 68, 0, -41, 66, -15, -27,
        -23, -9, -68, 37, 45, -69, 57, 80, 10, -64, 35, 26, 55, -67, 31, -76, 36, -99, 21]
# nums=[1]
# nums = [1,2]
nums = [-1, 1, 4, -4, 3, 5, 4, -2, 3, -1]
k = 3
print(Solution().topKFrequent(nums, k))
