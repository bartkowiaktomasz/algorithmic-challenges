import sys
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # Given:
        # .... 4 3 6 5 2 1
        # Scan right-to-left:
        # Swap first decreasing elem from the right: (3) with the first biggest elem to its right (5)
        # (We cannot swap with a smaller element as this would give a lexicographically smaller permutation)
        # .... 4 5 6 3 2 1
        # [...6 3 2 1] must be increasing (right-to-left) -> reverse it to get lexicographically smallest
        # permutation
        """
        larger_idx = None
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                larger_idx = i + 1
                for j in range(i + 2, len(nums)):
                    larger_idx = j if (nums[j] > nums[i]) and nums[j] <= nums[larger_idx] else larger_idx
                break
        if larger_idx is not None:
            nums[i], nums[larger_idx] = nums[larger_idx], nums[i]
            nums[:] = nums[:i + 1] + nums[i + 1:][::-1]
        else:
            # Strictly decreasing sequence e.g. [3, 2, 1]
            # Reverse in place
            nums[:] = nums[::-1]

sol = Solution()
nums = [1, 3, 2]  # -> 2, 1, 3
nums2 = [2,3,1,3,3] # -> [2,3,3,1,3]

sol.nextPermutation(nums2)
print(
    nums2
)
