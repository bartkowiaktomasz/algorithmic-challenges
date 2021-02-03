class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = [[-1 for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        # Every string is invalid for an empty pattern (apart from empty str)
        for i in range(len(s) + 1):
            memo[i][0] = False
        memo[0][0] = True

        for j in range(1, len(p) + 1):
            p_idx = j - 1
            if p[p_idx] == "*":
                memo[0][j] = memo[0][j - 1]
            else:
                memo[0][j] = False

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                s_idx = i - 1
                p_idx = j - 1
                if p[p_idx] == "*":
                    memo[i][j] = memo[i - 1][j - 1] or memo[i - 1][j] or memo[i][j - 1]
                elif p[p_idx] == "?":
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    if p[p_idx] == s[s_idx]:
                        memo[i][j] = memo[i - 1][j - 1]
                    else:
                        memo[i][j] = False

        return memo[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.isMatch("aa", "a") is False
    assert sol.isMatch("aa", "*") is True
    assert sol.isMatch("cb", "?") is False
    assert sol.isMatch("adceb", "*a*b") is True
    assert sol.isMatch("acdcb", "a*c?b") is False
