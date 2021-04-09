class Solution:
    def canDecode(self, s: str) -> bool:
        if int(s[0]) == 0:
            return False
        else:
            return 1 <= int(s) <= 26
    
    def numDecodings(self, s: str) -> int:
        dp = [None for _ in range(len(s) + 1)]
        dp[0] = 1
        def solve(s: str, num_decodings: int) -> int:
            if dp[len(s)] is None:
                x, y = 0, 0
                if self.canDecode(s[0]):
                    x = solve(s[1:], num_decodings)
                if len(s) >= 2 and self.canDecode(s[:2]):
                    y = solve(s[2:], num_decodings)
                dp[len(s)] = x + y
            return dp[len(s)]
        solve(s, 0)
        return dp[-1]


sol = Solution()
s = "111111111111111111111111111111111111111111111"
print(
    sol.numDecodings(s)
)