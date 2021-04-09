"""
Given an integer array `nums`, find the contiguous subarray (containing at 
least one number) which has the largest sum and return its sum.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Return maximum subarray sum.
        Note: This method also keeps track of indices of the array that gives
        the output sum: low_max_sum, high_max_sum
        """
        low_max_sum = 0
        high_max_sum = 0
        max_sum = nums[0]
        low = 0
        high = 0
        running_sum = nums[0]
        for i, n in enumerate(nums):
            if high == i - 1:
                # Add n to subarray even if it decreases running sum as long as
                # it does not cause it to drop below zero
                if running_sum >= 0:
                    if running_sum + n >= 0:
                        high += 1
                        running_sum += n
                else:
                    # If running sum is already < 0 start new subarray at i
                    #  if n is "less negative"
                    if n >= running_sum:
                        low = i
                        high = i
                        running_sum = n
            else:
                # Start new subarray if n is positive or "less negative" than
                #  current running sum
                if n >= running_sum or n >= 0:
                    low = i
                    high = i
                    running_sum = n

            if running_sum > max_sum:
                low_max_sum = low
                high_max_sum = high
                max_sum = running_sum

        return max_sum


sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(
    sol.maxSubArray(nums)
)