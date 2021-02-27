from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_first_row_zero = any(cell == 0 for cell in matrix[0])
        is_first_column_zero = any(row[0] == 0 for row in matrix)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    # If a given cell is 0, mark it in the corresponding cells
                    #  in the first row and first column
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                # Set the entire column to 0
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                # Set the entire row to 0
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        if is_first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if is_first_column_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol = Solution()
sol.setZeroes(matrix)
print(matrix)