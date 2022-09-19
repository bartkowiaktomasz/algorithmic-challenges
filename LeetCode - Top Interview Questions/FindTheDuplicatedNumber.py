from re import L
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Since the integers are in range `1, ..., n` we can jump around the array to 
        a position indicated by a current index `i`. One number will be duplicated 
        so there will be a cycle. Use Floyd's cycle detection algorithm to find a duplicate.

        Why there is a cycle?
        Since there is a duplicate, two (or more) numbers will point to that index in the array.
        We will first visit this index, follow the path and then visit it again, so there must be
        a cycle. 
        """
        slow, fast = 0, 0
        first_iter = True
        while first_iter or slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
            first_iter = False
        # slow met with fast, reset slow
        slow = 0
        while slow != fast:
            fast = nums[fast]
            prev = slow
            slow = nums[slow]
        return nums[prev]



sol = Solution()
nums =  [1, 2, 2, 3]
print(
    sol.findDuplicate(nums)
)