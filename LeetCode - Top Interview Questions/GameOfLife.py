from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_num_live_neighbours(board: List[List[int]], x: int, y: int):
            count = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if x == i and y == j:
                        continue
                    else:
                        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                            continue
                        if board[i][j] == 1 or board[i][j] == 3:
                            # 3 is 1 that will be set to 0
                            # 2 is 0 be set to 1
                            count += 1
            return count

        for i in range(0, len(board)):  # row
            for j in range(0, len(board[0])):  # column
                num_live_neighbours = get_num_live_neighbours(board, i, j)
                if board[i][j] == 1:
                    if num_live_neighbours < 2:
                        board[i][j] = 3
                    elif num_live_neighbours in [2, 3]:
                        pass  # keep 1
                    else:
                        board[i][j] = 3
                else:
                    if num_live_neighbours == 3:
                        board[i][j] = 2
        for i in range(0, len(board)):  # row
            for j in range(0, len(board[0])):  # column
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

sol = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol.gameOfLife(board)
print(board)