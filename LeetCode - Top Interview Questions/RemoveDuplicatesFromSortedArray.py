from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        slow = 1
        # forward i for it to point to the first duplicate
        while nums[slow] != nums[slow - 1]:
            slow += 1
            if slow == len(nums): return slow
        if nums[slow] != nums[slow - 1]: return slow
        # elem at idx i is a duplicate
        fast = slow
        while fast < len(nums):
            while nums[fast] <= nums[slow - 1]:
                fast += 1
                if fast == len(nums): return slow
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
            fast += 1
        return slow


s = Solution()
nums = []
s.removeDuplicates(nums)
print(nums)
