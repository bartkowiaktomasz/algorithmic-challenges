import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = sys.maxsize
        i, j, cur_sum = 0, 1, nums[0]
        while i < j:
            if cur_sum >= target:
                res = min(res, j - i)
            if cur_sum - nums[i] >= target:
                cur_sum -= nums[i]
                i += 1
            elif j < len(nums):
                cur_sum += nums[j]
                j += 1
            else: break
        if res == sys.maxsize:
            if cur_sum >= target: return len(nums)
            else: return 0
        else: return res

sol = Solution()
print(
    sol.minSubArrayLen(5, [2,3,1,1,1,1,1])
)