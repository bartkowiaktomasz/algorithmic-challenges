class Solution:
    def is_true_dp(self, dp, i, j, s, p):
        if (s[i - 1] == p[j - 1]) or (p[j - 1] == "."):
            # If letters match - assign a diagonal neighbour (i.e. as if we removed
            #  the character from both string and the pattern)
            return dp[i - 1][j - 1]
        if p[j - 1] == "*":
            # dp[i][j - 2] -> We ignore the pattern
            #   e.g. s = "x", p="xy*" <==> s = "x", p="x"
            if dp[i][j - 2]:
                return True
            if s[i - 1] == p[j - 2] or p[j - 2] == ".":
                # dp[i-1][j] -> We remove the character
                #  e.g. s = "xyy", p="xy*" <==> s = "xy", p="xy*"
                #  we can only remove character if it matches *
                return dp[i - 1][j]
        return False


    def isMatch(self, s: str, p: str) -> bool:
        num_rows = len(s) + 1
        num_cols = len(p) + 1
        dp = [
            [False for _ in range(num_cols)] for _ in range(num_rows)
        ]
        # Empty string and empty pattern is True
        dp[0][0] = True
        # Empty pattern gives False for everything but empty string
        for i in range(1, num_rows):
            dp[i][0] = False
        # Empty string might match e.g. "*a"
        for j in range(1, num_cols):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
            else:
                dp[0][j] = False
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                dp[i][j] = self.is_true_dp(dp, i, j, s, p)
        return dp[-1][-1]


sol = Solution()
args = [
    ("aa", "a"),  # False
    ("aa", "a*"),  # True
    ("ab", ".*"),  # True
    ("aab", "c*a*b"),  # True
    ("mississippi", "mis*is*p*."),  # False
    ("mississippi", "mis*is*ip*."),  # True
    ("aaa", "a*a"),  # True
    ("ab", ".*c"),  # False
    ("aaa", "ab*ac*a"),  # True
    ("aaa", "ab*a*c*a")  # True
]

print(
    [sol.isMatch(s, p) for s, p in args]
)
