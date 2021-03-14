from typing import List

class Solution:
    def bfs(self, i: int, j: int, visited: List[List[int]], board: List[List[str]]):
        n = len(board)
        m = len(board[0])
        queue = set([(i, j)])
        temp = set()
        visited[i][j] = True
        # K stands for "keep", i.e. this element should not be captured
        board[i][j] = 'K'
        while queue:
            x, y = queue.pop()
            if x + 1 < n and not visited[x + 1][y] and board[x + 1][y] == 'O':
                board[x + 1][y] = 'K'
                visited[x + 1][y] = True
                queue.add((x + 1, y))
            if x - 1 >= 0 and not visited[x - 1][y] and board[x - 1][y] == 'O':
                board[x - 1][y] = 'K'
                visited[x - 1][y] = True
                queue.add((x - 1, y))
            if y + 1 < m and not visited[x][y + 1] and board[x][y + 1] == 'O':
                board[x][y + 1] = 'K'
                visited[x][y + 1] = True
                queue.add((x, y + 1))
            if y - 1 >= 0 and not visited[x][y - 1] and board[x][y - 1] == 'O':
                board[x][y - 1] = 'K'
                visited[x][y - 1] = True
                queue.add((x, y - 1))
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in [0, n - 1]:
            for j in range(m):
                if not visited[i][j] and board[i][j] == 'O':
                    self.bfs(i, j, visited, board)
        for i in range(1, n - 1):
            for j in [0, m - 1]:
                if not visited[i][j] and board[i][j] == 'O':
                    self.bfs(i, j, visited, board)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == "K":
                    board[i][j] = 'O'
        return board
        
sol = Solution()
board = [["O","O","O"],["O","O","O"],["O","O","O"]]
print(
    sol.solve(board)
)