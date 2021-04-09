class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = 1
        for i in range(m):
            for j in range(n):
                row = (m - 1) - i
                col = (n - 1) - j
                if row < m - 1:
                    # Move down
                    dp[row][col] += dp[row + 1][col]
                if col < n - 1:
                    # Move right
                    dp[row][col] += dp[row][col + 1] 
        return dp[0][0]


sol = Solution()
print(
    sol.uniquePaths(3, 7)
)