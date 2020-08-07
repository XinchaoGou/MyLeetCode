from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        cnt = 0
        for l in range(length,1,-2):
            row = cnt
            cur_len = l - 1
            for col in range(cur_len):
                ul = matrix[row][col+row]
                ur = matrix[col+row][cur_len+row]
                br = matrix[cur_len+row][cur_len-col+row]
                bl = matrix[cur_len-col+row][row]
                matrix[row][col+row] = bl
                matrix[col+row][cur_len+row] = ul
                matrix[cur_len+row][cur_len-col+row] = ur
                matrix[cur_len-col+row][row+row]  = br
            cnt += 1

print(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))