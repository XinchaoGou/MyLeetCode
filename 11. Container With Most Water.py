from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right = len(height)-1
        max_area = 0
        while left < right:
            min_height = min(height[left], height[right])
            area = (right - left) * min_height
            max_area = max(area, max_area)
            if min_height == height[left]:
                left += 1
            else:
                right -= 1
        return max_area