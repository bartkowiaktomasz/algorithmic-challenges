from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = n - 1
        i = m - 1
        k = m + n - 1  # insert idex
        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j += -1
            else:
                nums1[k] = nums1[i]
                i += -1
            k += -1
        if i < 0:
            nums1[:j + 1] = nums2[:j + 1]


s = Solution()
nums1 = [1]
m = 1
nums2 = []
n = 0
s.merge(nums1, m, nums2, n)
print(nums1)