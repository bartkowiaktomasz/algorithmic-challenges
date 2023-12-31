from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i, j = 0, len(nums) - 1
        while j > i:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j += -1
            else:
                i += 1
        return i if nums[i] == val else i + 1

sol = Solution()
nums, val = [3,2,2,3], 3
print(sol.removeElement(nums, val), nums)
nums, val = [0,1,2,2,3,0,4,2], 2
print(sol.removeElement(nums, val), nums)