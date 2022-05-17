from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = {}
        cur_path = set()
        def _dfs(x: int, y: int):
            nonlocal matrix
            nonlocal cur_path
            cur_path.add((x, y))
            max_ = 1
            for i, j in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
                if i < 0 or i >= n or j < 0 or j >= m:
                    continue
                if matrix[i][j] > matrix[x][y]:
                    if (i, j) in dp:
                        max_ = max(max_, 1 + dp[(i, j)])
                    elif (i, j) not in cur_path:
                        max_ =  max(max_, 1 + _dfs(i, j))
            dp[(x, y)] = max_
            cur_path.remove((x ,y))
            return max_
        return max([_dfs(i, j) for i in range(n) for j in range(m)])

matrix = [[3,4,5],[3,2,6],[2,2,1]]
sol = Solution()
print(
    sol.longestIncreasingPath(matrix)
)