class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleaveBottomUp(s1, s2, s3)

    def isInterleaveTopDown(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False
        memo = {}
        def dp(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2): return True
            else:
                if (i, j) in memo: return memo[(i, j)]
                else:
                    res = []
                    if i < len(s1) and s1[i] == s3[i + j]: res.append(dp(i + 1, j))
                    if j < len(s2) and s2[j] == s3[i + j]: res.append(dp(i, j + 1))
                    memo[(i, j)] = any(res)
                    return memo[(i, j)]
        return dp(0, 0)

    def isInterleaveBottomUp(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False
        memo = {}
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i == len(s1) and j == len(s2): memo[(i, j)] = True
                else:
                    if i == len(s1): memo[(i, j)] = memo[(i, j + 1)] if s3[i + j] == s2[j] else False
                    elif j == len(s2): memo[(i, j)] = memo[(i + 1, j)] if s3[i + j] == s1[i] else False
                    else: 
                        res = []
                        if s3[i + j] == s2[j]: res.append(memo[i, j + 1])
                        if s3[i + j] == s1[i]: res.append(memo[i + 1, j])
                        memo[(i, j)] = any(res)
        return memo[(0, 0)]

s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbcbcac"
sol = Solution()
print(
    sol.isInterleave(s1, s2, s3)
)