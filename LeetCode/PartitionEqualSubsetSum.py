from re import S
from typing import List


class Solution:
    def _canPartition_td(self, nums: List[int]) -> bool:
        """
        Top-down
        """
        sum_ = sum(nums)
        if sum_ % 2 == 1: return False
        target = sum_ // 2
        dp = [[None for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for j in range(target + 1): dp[0][j] = False
        for i in range(len(nums) + 1): dp[i][0] = True
        def solve(i: int, j: int):
            nonlocal dp, nums
            if dp[i][j] is not None: return dp[i][j]
            x = solve(i - 1, j)
            y = solve(i - 1, j - nums[i - 1])
            dp[i][j] = x or y
            return dp[i][j]
        solve(len(nums), target)
        return dp[-1][-1]

    def _canPartition_bu(self, nums: List[int]) -> bool:
        """
        Bottom-up
        """
        sum_ = sum(nums)
        if sum_ % 2 == 1: return False
        target = sum_ // 2
        dp = [[None for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for j in range(target + 1): dp[0][j] = False
        for i in range(len(nums) + 1): dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j] or j >= nums[i - 1] and dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]

    def canPartition(self, nums: List[int]) -> bool:
        return self._canPartition_td(nums)

nums = [1,5,11,5]
nums2 = [1,2,3,5]
nums3 = [1,2,5]
nums4 = [1,2,3,4,5,6,7]
nums5 = [100]
sol = Solution()
print(
    sol.canPartition(nums5)
)
        