from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[high - 1] > nums[high]:
                return nums[high]
            if nums[mid] > nums[0]:
                low = mid + 1
            else:
                high = mid
        return nums[0]


sol = Solution()
nums = [11,13,15,17,18]
nums2 = [5,1,2,3,4]
nums3 = [3,4,5,1,2]
nums4 = [4,5,6,7,0,1,2]
nums5 = [11,13,15,17]
nums6 = [11,13,15,17,18]
nums7 = [2,1]
nums8 = [2,3,1]
print(
    sol.findMin(nums)
)