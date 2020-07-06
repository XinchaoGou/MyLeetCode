from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0

        nums = 0
        s_d = {}
        merge = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                v = grid[i][j]
                if v != '0':
                    u = '0' if i == 0 else s_d.get(grid[i - 1][j], grid[i - 1][j])
                    l = '0' if j == 0 else s_d.get(grid[i][j - 1], grid[i][j - 1])
                    if l != '0':  # extend island
                        if u != '0':
                            if l != u:  # merge to the island of last line
                                min_lu = min(int(l), int(u))
                                grid[i][j] = min_lu
                                s_d[u] = min_lu
                                s_d[l] = min_lu
                                merge += 1
                                continue
                        grid[i][j] = l
                        continue
                    if u != '0':
                        grid[i][j] = u
                    else:
                        nums += 1
                        grid[i][j] = str(nums)
        return nums - merge


input = [
    ['1', '0', '1', '1', '0'],
    ['0', '1', '1', '0', '0'],
    ['1', '1', '1', '0', '1'],
    ['0', '0', '1', '1', '1']]

# input = [
#     [1, 0, 1, 0, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 1],
# ]

output = Solution().numIslands(input)
print(output)
