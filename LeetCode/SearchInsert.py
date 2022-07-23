from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid
            else:
                i = mid + 1
        return i

nums = [1,3,5,6]
target = 0
sol = Solution()
print(
    sol.searchInsert(nums, target)
)