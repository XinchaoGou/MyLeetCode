from typing import List

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         if numRows <= 0:
#             return []
#         if numRows == 1:
#             return [[1]]
#         last_triangle = self.generate(numRows - 1)
#         last_line = last_triangle[-1]
#         new_line = []
#         new_line.append(1)
#         for i in range(len(last_line)-1):
#             new_line.append(last_line[i] + last_line[i+1])
#         new_line.append(1)
#         last_triangle.append(new_line)
#         return last_triangle

class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle



input = 5
output = Solution().generate(input)
print(output)