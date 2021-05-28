"""
Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value.

If target is not found in the array, return `[-1, -1]`.
"""
import math
from typing import List


class Solution:
    def binary_search_leftmost(self, nums: List[int], elem: int):
        """
        Return leftmost index of `elem` if it exists in `nums`, otherwise return -1
        """
        low = 0
        high = len(nums) - 1
        while high > low:
            mid = (high + low) // 2
            if nums[mid] >= elem:
                high = mid
            else:
                low = mid + 1
        if nums and nums[low] == elem:
            return low
        return -1

    def binary_search_rightmost(self, nums: List[int], elem: int):
        """
        Return rightmost index of `elem` if it exists in `nums`, otherwise return -1
        """
        low = 0
        high = len(nums) - 1
        while high > low:
            mid = math.ceil((high + low) / 2)
            if nums[mid] > elem:
                high = mid - 1
            else:
                low = mid
        if nums and nums[low] == elem:
            return high
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.binary_search_leftmost(nums, target)
        r = self.binary_search_rightmost(nums, target)
        return [l, r]


sol = Solution()
arr = [5, 7, 7, 8, 8, 10]
print(
    sol.searchRange([], 6)
)
