"""
 You are given an integer array `nums` sorted in ascending order (with distinct values),
and an integer target.

Suppose that `nums` is rotated at some pivot unknown to you beforehand
(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

If target is found in the array return its index, otherwise, return `-1`.
"""
import sys
from typing import List


class Solution:
    def is_pivot(self, nums, idx):
        """Pivot is first element after pivoting, e.g. for [3, 4, 5, 1, 2] pivot is 1"""
        if idx == 0:
            return False  # Pivot is guaranteed to exist
        if idx + 1 == len(nums):
            if nums[idx - 1] <= nums[idx]:
                return False
            else:
                return True
        if nums[idx - 1] > nums[idx] < nums[idx + 1]:
            return True
        else:
            return False


    def find_pivot(self, nums: List[int]):
        """
        Find index of pivot (see is_pivot) if it exists, otherwise the array is sorted
        and return max integer.
        """
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = low + (high - low) // 2
            if self.is_pivot(nums, mid):
                return mid
            if nums[mid] >= nums[0]:
                low = mid + 1
            else:
                high = mid - 1
        # no pivot exists -> array is sorted
        return sys.maxsize

    def binary_search(self, nums: List[int], elem: int):
        """
        Find an index of `elem` if it exists in `nums`, otherwise return -1
        """
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] == elem:
                return mid
            if nums[mid] > elem:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        """
        Find the index of `target` in the input array `nums`
        Pseudocode:
        1. Find the index of the pivot
        2. Perform binary search in either left or right sublist

        Note: If pivot does not exist, set pivot to max integer and do a binary search
        over the entire list
        """
        pivot_idx = self.find_pivot(nums)
        if target >= nums[0]:
            return self.binary_search(nums[0:pivot_idx], target)
        else:
            idx = self.binary_search(nums[pivot_idx:], target)
            return idx if idx == -1 else pivot_idx + idx


s = Solution()
print(
    s.search([1, 1], 1)
)
