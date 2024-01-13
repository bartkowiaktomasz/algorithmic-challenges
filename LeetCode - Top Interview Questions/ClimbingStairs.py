class Solution:
    def climbStairs(self, n: int) -> int:
        # DP state: dp[n] = dp[n - 1] + dp[n - 2]
        if n == 1: return 1
        if n == 2: return 2
        i, j = 1, 2
        for _ in range(3, n + 1):
            i, j = j, j + i
        return j

s = Solution()
print(
    s.climbStairs(4)
)
            