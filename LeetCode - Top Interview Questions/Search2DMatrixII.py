from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])
        i, j = 0, w - 1  # top-right corner
        while (0 <= i < h) and (0 <= j < w):
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j += -1
            else:
                i += 1
        return False


sol = Solution()

matrix = [[1,1]]
target = 1
print(
    sol.searchMatrix(matrix, target)
)