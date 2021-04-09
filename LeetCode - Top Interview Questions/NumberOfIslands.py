from typing import List

class Solution:
    def bfs(self, grid: List[List[str]], i: int, j: int):
        n, m = len(grid), len(grid[0])
        queue = set()
        queue.add((i, j))
        while queue:
            i, j = queue.pop()
            if not (i >= 0 and j >= 0 and i < n and j < m and grid[i][j] == '1'):
                continue
            grid[i][j] = 'V'  # Visited
            queue.add((i - 1, j))
            queue.add((i + 1, j))
            queue.add((i, j - 1))
            queue.add((i, j + 1))

    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        num_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '1':
                    continue
                self.bfs(grid, i, j)
                num_islands += 1
        return num_islands


sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(
    sol.numIslands(grid)
)