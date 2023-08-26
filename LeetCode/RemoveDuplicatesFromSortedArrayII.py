from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        if len(nums) == 2: return 2
        i = 0
        # Mark duplicates as "_"
        while i < len(nums):
            i += 2
            while i < len(nums) and nums[i] != nums[i - 2]:
                i += 1
            dup = nums[i - 2]
            while i < len(nums) and nums[i] == dup:
                nums[i] = "_"
                i += 1
        i, j = 0, 0
        # Replace "_" pointed by i with character at j
        # i is a slow pointer, j is a fast pointer
        while (i < len(nums)) and (j < len(nums)):
            if nums[i] != "_":
                i += 1
                j += 1
            else:
                while j < len(nums) and nums[j] == "_":
                    j += 1
                if j == len(nums): break
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        return i
        


sol = Solution()
nums = [1,1,1]
print(
    sol.removeDuplicates(nums)
)
print(
    nums
)