from typing import List


class Solution:
    def swap(self, i: int, j: int, nums: List[int]):
        nums[i], nums[j] = nums[j], nums[i]

    def partition(self, low: int, high: int, nums: List[int]) -> int:
        """
        Find index "j" of a partition (pivot) element. j is such that any element at
        index i < j is smaller than pivot, and any index i > j is greater or equal to
        pivot
        """
        pivot = nums[low]
        i = low + 1
        j = high
        while j >= i:
            if nums[i] >= pivot > nums[j]:
                self.swap(i, j, nums)
            elif nums[i] >= pivot:
                j -= 1
            elif nums[j] < pivot:
                i += 1
            else:
                j -= 1
                i += 1
        self.swap(low, j, nums)
        return j

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = k - 1  # 1st largest -> 0th largest
        m = (len(nums) - 1) - k  # kth largest == mth smallest
        i, j = 0, len(nums) - 1
        while True:
            idx = self.partition(i, j, nums)
            if idx == m:
                return nums[idx]
            if idx > m:
                j = idx - 1
            else:
                i = idx + 1

sol = Solution()
nums = nums = [3,2,1,5,6,4]
k = 2
print(
    sol.findKthLargest(nums, k)
)