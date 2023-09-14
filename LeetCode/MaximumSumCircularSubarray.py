from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        cur_min, cur_max, min_sum, max_sum = nums[0], nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            cur_min = min(cur_min + nums[i], nums[i])

            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)

        if min_sum == total: return max_sum
        else: return max(max_sum, total - min_sum)

s = Solution()
nums = [1,-2,3,-2]
nums = [5,-3,5]
print(
    s.maxSubarraySumCircular(nums)
)