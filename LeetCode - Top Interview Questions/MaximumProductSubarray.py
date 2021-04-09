import math
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_, min_, res = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            print(max_)
            if num < 0:
                # If num is negative, the new min can be calculated from current max     
                min_, max_ = min(num, max_ * num), max(num, min_ * num)
            else:
                min_, max_ = min(num, min_ * num), max(num, max_ * num)
            res = max(res, max_, num)
        return res
            
            
        
sol = Solution()
nums = [-2,0,-1] # -12 -4 -2
print(
    sol.maxProduct(nums)
)