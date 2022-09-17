from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [1 if matrix[0][j] == '1' else 0 for j in range(m)]
        prev = dp[-1]
        max_ = 1 if any([e == 1 for e in dp]) else 0
        for i in range(1, n):
            dp[-1] = prev
            for j in range(m):
                if j == 0:
                    prev = 1 if matrix[i][j] == '1' else 0
                else:
                    new = 0 if matrix[i][j] == '0' else (
                        1 + min(prev, dp[j - 1], dp[j])
                    )
                    dp[j - 1], prev = prev, new
                max_ = max(max_, prev)
        return max_ * max_

sol = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix2 = [["1","0","1"],["0","1","1"],["0","1","1"]]
matrix3 = [["0"],["1"]]
print(
    sol.maximalSquare(matrix)
)