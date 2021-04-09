"""
Given an `m x n` matrix, return all elements of the matrix in spiral order.
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left_bound = -1
        right_bound = len(matrix[0])
        upper_bound = -1
        lower_bound = len(matrix)
        row, col = 0, 0
        direction = (0, 1)
        res = []
        while True:
            while (
                col != left_bound
                and col != right_bound
                and row != upper_bound
                and row != lower_bound
            ):
                res.append(matrix[row][col])
                row += direction[0]
                col += direction[1]
            if len(res) == len(matrix) * len(matrix[0]):
                break
            row -= direction[0]
            col -= direction[1]
            if direction == (0, 1):
                # right -> down
                direction = (1, 0)
                upper_bound += 1
            elif direction == (1, 0):
                # down -> left
                direction = (0, -1)
                right_bound -= 1
            elif direction == (0, -1):
                # left -> up
                direction = (-1, 0)
                lower_bound -= 1
            else:
                # up -> right
                direction = (0, 1)
                left_bound += 1
            row += direction[0]
            col += direction[1]
        return res
        
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(
    sol.spiralOrder(matrix)
)