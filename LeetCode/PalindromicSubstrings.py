class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        # dp[i][j] = True => s[i:j + 1] is a palindrome, i = 0, ..., len(s) -1, j = 0, ..., len(s) - 1
        for i in range(len(s)): 
            dp[i][i] = True 
        res = 0
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if i != j:
                    if j - i >= 2:
                        dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                    else:
                        dp[i][j] = s[i] == s[j]
                res += bool(dp[i][j]) # i == j has been initialised to True
        return res

sol = Solution()
s = "abc"
s2 = "aaa"
print(
    sol.countSubstrings(s)
)
