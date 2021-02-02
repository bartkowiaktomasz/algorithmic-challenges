"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

Each row must contain the digits 1-9 without repetition. Each column must contain the
digits 1-9 without repetition. Each of the nine 3 x 3 sub-boxes of the grid must
contain the digits 1-9 without repetition.
"""
from typing import List


class Solution:
    SUDOKU_SIZE = 9

    def box_idx(self, i: int, j: int):
        return 3 * (i // 3) + (j // 3)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # indices 0 - 8 store elements in rows
        # indices 9 - 17 store elements in columns
        # indices 18 - 24 stpre elements in 3x3 boxes
        elems_map = [set() for _ in range(3 * Solution.SUDOKU_SIZE)]

        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem == ".":
                    continue
                elif 1 <= int(elem) <= 9:
                    if (
                            elem in elems_map[i] or
                            elem in elems_map[j + Solution.SUDOKU_SIZE] or
                            elem in elems_map[self.box_idx(i, j) + 2 * Solution.SUDOKU_SIZE]
                    ):
                        return False
                    else:
                        elems_map[i].add(elem)
                        elems_map[j + Solution.SUDOKU_SIZE].add(elem)
                        elems_map[self.box_idx(i, j) + 2 * Solution.SUDOKU_SIZE].add(elem)
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
