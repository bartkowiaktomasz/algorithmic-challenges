from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Return the number that appears once
        All other numbers appear 3 times
        """
        x0, x1 = 0, 0
        # x1 keeps track of numbers that appeared twice
        # x0 keeps track of numbers that appeared once
        for n in nums:
            # Add n to x0 if its not in x1
            x0 = (x0 ^ n) & ~x1
            # Add n to x1 if its not in x0 
            #  it must be the 2nd instance of "n"
            x1 = (x1 ^ n) & ~x0
        return x0

sol = Solution()
print(
    sol.singleNumber([2, 2, 3, 2, 5, 5, 5])
)