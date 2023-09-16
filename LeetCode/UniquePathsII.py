from collections import deque
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        unique_paths = [[0 for _ in range(n)] for _ in range(m)]
        unique_paths[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: continue
                if i - 1 >= 0: unique_paths[i][j] += unique_paths[i - 1][j]
                if j - 1 >= 0: unique_paths[i][j] += unique_paths[i][j - 1]
        return unique_paths[-1][-1]
    
sol = Solution()
print(
    sol.uniquePathsWithObstacles([[1]])
)