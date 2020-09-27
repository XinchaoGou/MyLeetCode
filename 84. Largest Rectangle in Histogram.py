from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            val = heights[i]
            left = 0
            for j in range(i, -1,-1):
                if heights[j]<val:
                    left = j +1
                    break
            right = len(heights)
            for j in range(i, len(heights)):
                if heights[j]<val:
                    right = j
                    break
            res = max(res, val*(right-left))
        return res


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        return max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                right[stack[-1]] = i
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        return max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0

input = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(input))