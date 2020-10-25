from typing import List
# class Solution:
#     def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
#         tree = [[] for _ in range(N)]
#         for father, child in edges:
#             tree[father].append(child)
#             tree[child].append(father)
#         depth = [0 for _ in range(N)]
#         count = [0 for _ in range(N)]
#
#
#         def dfsForDepthAndCount(node, father):
#             count[node] = 1
#             for child in tree[node]:
#                 if child != father:
#                     depth[child] = depth[node] + 1
#                     dfsForDepthAndCount(child, node)
#                     count[node] += count[child]
#
#
#         dfsForDepthAndCount(0, -1)
#         answer = [0 for _ in range(N)]
#         answer[0] = sum(depth)
#
#
#         def dfsForAnswer(root, father):
#             for child in tree[root]:
#                 if child != father:
#                     answer[child] = answer[root] + N - 2 * count[child]
#                     dfsForAnswer(child, root)
#
#
#         dfsForAnswer(0, -1)
#         return answer

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(N)]
        for edge in edges:
            father, child = edge
            graph[father] += [child]
            graph[child] += [father]


N = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
print(Solution().sumOfDistancesInTree(N, edges))
