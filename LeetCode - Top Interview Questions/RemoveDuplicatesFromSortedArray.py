from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        while nums:
            if i == l - 1:
                break
            if nums[i + 1] == nums[i]:
                del nums[i]  # O(N)
                l -= 1
            else:
                i += 1
        return len(nums)


s = Solution()
nums = []
s.removeDuplicates(nums)
print(nums)
