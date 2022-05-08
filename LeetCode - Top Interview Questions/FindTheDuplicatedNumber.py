from re import L
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
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
nums =  [2,2,2,2]
print(
    sol.findDuplicate(nums)
)