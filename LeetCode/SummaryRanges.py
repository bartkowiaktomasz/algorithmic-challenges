from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
      if not nums: return []
      out, i, j = [], 0, 0
      while j < len(nums):
         while j < len(nums) - 1 and nums[j + 1] == nums[j] + 1:
            j += 1
         if i == j:
            out.append(f"{nums[i]}")
            i += 1
            j += 1
         else:
            out.append(f"{nums[i]}->{nums[j]}")
            j += 1
            i = j
      return out

nums = [0,2,3,4,6,8,9]
sol = Solution()
print(
   sol.summaryRanges(nums)
)