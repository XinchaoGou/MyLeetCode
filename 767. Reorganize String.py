import collections
import heapq

# class Solution(object):
#     def reorganizeString(self, S):
#         N = len(S)
#         A = []
#         for k,v in sorted(collections.Counter(S).items(), key=lambda x:x[1], reverse=True):
#             if v > (N+1)/2: return ''
#             A.extend(k * v)
#         ans = [None] * N
#         # ans[::2], ans[1::2] = A[N//2:], A[:N//2]
#         # print(len(ans[::2]), len(ans[1::2]), len(A[(N+1) // 2:]), len( A[:(N+1) // 2]))
#         ans[::2], ans[1::2] = A[:(N+1)//2], A[(N+1)//2:]
#         return "".join(ans)


# 贪心堆
class Solution(object):
    def reorganizeString(self, S):
        hq = sorted([(-v, k) for k, v in collections.Counter(S).items()])
        heapq.heapify(hq)
        N = len(S)
        if any(-nc > (N + 1) // 2 for nc, k in hq):
            return ''

        ans = []
        while len(hq) >= 2:
            nc1, c1 = heapq.heappop(hq)
            nc2, c2 = heapq.heappop(hq)
            ans.extend([c1, c2])
            if nc1 + 1: heapq.heappush(hq, (nc1 + 1, c1))
            if nc2 + 1: heapq.heappush(hq, (nc2 + 1, c2))
        return "".join(ans) + (hq[0][1] if hq else "")

S = "aab"
S = "abbabbaaab"
# S = "vvvlo"
print(Solution().reorganizeString(S))