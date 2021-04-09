from typing import List

class Solution:
    def swap(self, nums: List[int], i: int, j: int):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        mid = 0
        right = len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                self.swap(nums, left, mid)
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                self.swap(nums, mid, right)
                right -= 1
            

sol = Solution()
nums = [2,0,1]
sol.sortColors(nums)