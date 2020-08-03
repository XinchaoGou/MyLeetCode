from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    p+=4
                    if i >= 1 and grid[i-1][j]:
                        p -=2
                    if j >= 1 and grid[i][j-1]:
                        p -=2
        return p