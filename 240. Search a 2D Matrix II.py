class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        bottom = len(matrix) - 1
        left = 0
        n = len(matrix[0])
        while bottom>=0 and left<n:
            if matrix[bottom][left] > target:
                bottom -= 1
            elif matrix[bottom][left] < target:
                left += 1
            else:
                return True
        return False