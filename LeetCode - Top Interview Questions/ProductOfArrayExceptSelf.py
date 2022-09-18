import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(n)]
        res[0] = nums[0]
        # Calculate cum product
        for i in range(1, n):
            res[i] = nums[i] * res[i - 1]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i - 1] * right if i > 0 else right
            right *= nums[i]
        return res


sol = Solution()
nums = [-1,1,1,-3,3]
nums2 = [1,2,3,4]
nums3 = [-1,1,0,-3,3]
print(
    sol.productExceptSelf(nums3)
)