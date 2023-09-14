"""
Given an integer array `nums`, find the contiguous subarray (containing at 
least one number) which has the largest sum and return its sum.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Return maximum subarray sum using Kadane's algorithm
        Note: This method also keeps track of indices of the array that gives
        the max output sum
        """
        low, high, max_sum, cur_sum = 0, 0, float('-inf'), 0
        for i, n in enumerate(nums):
            cur_sum += n
            if cur_sum > max_sum:
                max_sum = cur_sum
                high = i
            if cur_sum < 0:
                cur_sum = 0
                low = i + 1
        return max_sum


sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [5,4,-1,7,8]
print(
    sol.maxSubArray(nums)
)