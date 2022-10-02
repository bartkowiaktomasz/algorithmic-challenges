class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # padding strings with empty character at the beginning
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                dp[i][j] = (
                    # text1 and text2 are "1-indexed" because of padding, thus
                    #  text2[j - 1] == text1[i - 1]
                    1 + dp[i - 1][j - 1] if text2[j - 1] == text1[i - 1] else max(
                        dp[i][j - 1], dp[i - 1][j]
                    )
                )
        return dp[-1][-1]

sol = Solution()
text = ("abcde", "ace")
text2 = ("abc", "abc")
text3 = ("abc", "def")
print(
    sol.longestCommonSubsequence(*text3)
)