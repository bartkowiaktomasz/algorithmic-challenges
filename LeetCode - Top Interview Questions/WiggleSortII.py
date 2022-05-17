import math
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = math.ceil(len(nums) / 2)
        sorted_ = sorted(nums)
        # Split sorted numbers into left, right subarrays
        # Revert them to ensure we start with the highest from "left"
        # Otherwise input [4, 5, 5, 6] will give us [4, 5, 5, 6] which is wrong
        # because 5 is not < 5
        smaller, bigger = sorted_[:mid][::-1], sorted_[mid:][::-1]
        # Overwrite nums by replacing (alternatively) from smaller/bigger
        nums[::2] = smaller
        nums[1::2] = bigger

sol = Solution()
nums = [1,5,1,1,6,4]
nums = [4, 5, 5, 6]
sol.wiggleSort(nums)
print(
    nums
)
