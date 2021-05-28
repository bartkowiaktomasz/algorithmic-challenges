from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x0, x1 = 0, 0
        # x1 keeps track of numbers that appeared twice
        # x0 keeps track of numbers that appeared once
        for n in nums:
            # Add n to x0 if its not in x1
            x0 = (x0 ^ n) & ~x1
            # Add n to x1 if its not in x0 
            #  (if it was we'd had a number in both x0, x1 but we don't cause we 
            #   want to reset anything that appears 3 times)
            x1 = (x1 ^ n) & ~x0
        return x0

sol = Solution()
print(
    sol.singleNumber([2, 2, 3, 2, 5, 5, 5])
)