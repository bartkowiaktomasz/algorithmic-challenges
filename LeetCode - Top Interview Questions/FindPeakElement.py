from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, len(nums) - 1
        if n == 1:
            return 0
        def is_peak(i: int):
            if i == 0 and nums[1] < nums[0]:
                return True
            elif i == n - 1 and nums[n - 2] < nums[n - 1]:
                return True
            elif nums[i - 1] < nums[i] > nums[i + 1]:
                return True
            else:
                return False
        i = (low + high) // 2
        while not is_peak(i):
            if nums[i + 1] > nums[i]:
                low = i + 1
            else:
                high = i - 1    
            i = (low + high) // 2
        return i

sol = Solution()
nums = [1,2,1,3,5,6,4]
print(
    sol.findPeakElement(nums)
)