from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        dp = [None for _ in range(n)]
        dp[-1], dp[-2] = nums[-1], max(nums[-1], nums[-2])
        for i in range(n - 1 - 2, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0]

nums = [2,7,9,3,1]
sol = Solution()
print(
    sol.rob(nums)
)