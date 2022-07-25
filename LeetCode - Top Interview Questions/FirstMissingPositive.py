"""
Given an unsorted integer array `nums`, find the smallest missing positive integer
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        First missing positive must be in range [1, ... l + 1] where l is the length
        of the list. e.g. for list [1, 2, 3] the first missing positive is l + 1 = 4
        """
        # Cap all numbers > n and <= 0 and set to n + 1
        #   After this step we no longer have negative numbers
        #   This will allow us to do the -1 trick to mark numbers present in the 
        #   array
        n = len(nums)
        for i, elem in enumerate(nums):
            if elem > n or elem <= 0:
                nums[i] = n + 1
        # Here elements in `nums` must be in range [1, n] because we had changed all
        # other elements to n + 1
        for i, elem in enumerate(nums):
            # We do abs because we multiply other elements in the array by -1 later on
            #  while iterating
            if abs(elem) == n + 1:
                continue
            # We must have multiplied nums[abs(elem)] by -1 already, so
            #  elem is present in the array
            if nums[abs(elem) - 1] < 0:
                continue
            # Mark element (value at its index - 1) as present in the array
            nums[abs(elem) - 1] *= -1
        # Here the negative elements indicate which positive elements are present
        #  in the array. For example [-1, -2, 4] (original array [1, 2, 4])
        #  means that 1 and 2 must be present in the input array because numbers
        #  arr[1 - 1] = -2 and arr[2 - 1] = -2 are negative. First missing positive is 3
        #  because arr[3 - 1] > 0
        for i, elem in enumerate(nums):
            if elem > 0:
                return i + 1
        return len(nums) + 1


sol = Solution()
nums = [3, 3, 3]
print(
    sol.firstMissingPositive(nums)
)
