"""
Given an array of non-negative integers `nums`, you are initially positioned at
the first index of the array. Each element in the array represents your 
maximum jump length at that position. Determine if you are able to reach the 
last index.
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        leftmost_good = len(nums) - 1
        dp[leftmost_good] = True
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > len(nums) - 1:
                nums[i] = len(nums) - 1
            if i + nums[i] >= leftmost_good >= i:
                dp[i] = True
                leftmost_good = i
        return dp[0]

sol = Solution()
nums = [2,3,1,1,4]
print(
    sol.canJump(nums)
)