"""
You are given an `n x n` 2D matrix representing an image, rotate the image by 90 
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

from typing import List

class Solution:
    def reflect(self, matrix: List[int]):
        """
        Reflect input matrix around y-axis passing through
        the centre
        """
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                self.swap(matrix, i, j, i, (len(matrix) - 1) - j)

    def transpose(self, matrix: List[int]):
        for i in range(len(matrix)):
            for j in range(0, i):
                self.swap(matrix, i, j, j, i)

    def swap(self, matrix: List[int], i1: int, j1: int, i2: int, j2: int):
        """
        Swap matrix elements in place with XOR trick
        """
        matrix[i1][j1] = matrix[i1][j1] ^ matrix[i2][j2]
        matrix[i2][j2] = matrix[i2][j2] ^ matrix[i1][j1]
        matrix[i1][j1] = matrix[i1][j1] ^ matrix[i2][j2]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)

sol = Solution()
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sol.rotate(m)
print(m)
