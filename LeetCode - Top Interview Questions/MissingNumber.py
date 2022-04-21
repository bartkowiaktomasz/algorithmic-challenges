from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x1, x2 = 0, 0
        for i in range(len(nums) + 1):
            x1 ^= i
        for i in range(len(nums)):
            x2 ^= nums[i]
        # x1 contains all numbers 0,...,n
        # x2 contains all numbers 0,...,n but one (say "x")
        # x1^x2 will leave only "x"
        return x1 ^ x2
        