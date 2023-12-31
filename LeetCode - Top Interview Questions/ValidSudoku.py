"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

Each row must contain the digits 1-9 without repetition. Each column must contain the
digits 1-9 without repetition. Each of the nine 3 x 3 sub-boxes of the grid must
contain the digits 1-9 without repetition.
"""
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                elems = [(i, board[i][j]), (board[i][j], j), (i // 3, j // 3, board[i][j])]
                if any([
                    e in seen for e in elems
                ]):
                    return False
                for e in elems: seen.add(e)
        return True

board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]

sol = Solution()
print(
    sol.isValidSudoku(board)
)
