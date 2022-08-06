class Solution:
    dp = {0: 1, 1: 1}
    def numTrees(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        else:
            sum_ =  sum([
                self.numTrees(i - 1) * self.numTrees(n - i) for i in range(1, n + 1)
            ])
            self.dp[n] = sum_
            return sum_

sol = Solution()
print(
    sol.numTrees(4)
)
print(sol.dp)