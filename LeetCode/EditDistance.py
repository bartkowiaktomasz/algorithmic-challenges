import sys


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[sys.maxsize for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        def solve(i: int, j: int):
            nonlocal dp
            s1, s2 = word1[i:], word2[j:]
            if len(s1) == len(s2) and s1 == s2:
                dp[i][j] = 0
            elif len(s1) == 0 or len(s2) == 0:
                dp[i][j] = abs(len(s1) - len(s2))
            elif dp[i][j] < sys.maxsize:
                pass
            elif s1[0] == s2[0]:
                dp[i][j] = min(
                    1 + solve(1 + i, j),
                    1 + solve(i, j + 1),
                    solve(1 + i, j + 1),
                )
            else:
                dp[i][j] = min(
                    1 + solve(1 + i, j), 
                    1 + solve(1 + i, j + 1),
                    1 + solve(i, j + 1)
                )
            return dp[i][j]
        solve(0, 0)
        return dp[0][0]

sol = Solution()
word1 = "intention"
word2 = "execution"
print(
    sol.minDistance(word1, word2)
)

