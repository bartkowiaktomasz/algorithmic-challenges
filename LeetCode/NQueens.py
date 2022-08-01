import copy
from typing import List, Tuple


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def canAttack(x: Tuple[int, int], y: Tuple[int, int]) -> bool:
            if (x[0] == y[0] or x[1] == y[1] or abs(x[0] - y[0]) == abs(x[1] - y[1])):
                return True
            else:
                return False
        res = []
        stack = [(0, -1)]
        while stack:
            top = stack.pop()
            last = top[0] * n + top[1]
            for cell in range(last + 1, n * n):
                i, j = cell // n, cell % n
                for existing in stack:
                    if canAttack((i, j), existing):
                        break
                else:
                    stack.append((i, j))
                    if len(stack) == n:
                        res.append(copy.copy(stack))
        boards = []
        for r in res:
            board = [["." for _ in range(n)] for _ in range(n)]
            for p in r:
                board[p[0]][p[1]] = "Q"
            # concatenate dots with "Q"
            board = ["".join(row) for row in board]
            boards.append(board)
        return boards

sol = Solution()
print(
    sol.solveNQueens(5)
)