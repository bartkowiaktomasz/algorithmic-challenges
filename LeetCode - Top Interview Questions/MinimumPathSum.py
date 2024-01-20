import sys
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[sys.maxsize for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]
        def solve(i: int, j: int):
            if i >= len(grid) or j >= len(grid[0]):
                return sys.maxsize
            if dp[i][j] < sys.maxsize:
                return dp[i][j]
            else:
                dp[i][j] = grid[i][j] + min(
                    solve(i + 1, j), solve(i, j + 1)
                )
                return dp[i][j]
        solve(0, 0)
        return dp[0][0]

sol = Solution()
grid = [[1,2,3],[4,5,6]]
print(
    sol.minPathSum(grid)
)