class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        i = 1
        j = 2
        for _ in range(3, n + 1):
            i, j = j, j + i
        return j

s = Solution()
print(
    s.climbStairs(4)
)
            