from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Sapce can be optimised by only maintaining last two dp
        states: prev, cur:
        
        prev, cur = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tmp = cur
            cur = max(cur, prev + nums[i])
            prev = tmp
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

nums = [2,7,9,3,1]
sol = Solution()
print(
    sol.rob(nums)
)