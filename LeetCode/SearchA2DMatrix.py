from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1
        while True:
            if i >= len(matrix) or j < 0:
                return False
            guess = matrix[i][j]
            if guess == target:
                return True
            elif guess > target:
                j += -1
            else:
                i += 1