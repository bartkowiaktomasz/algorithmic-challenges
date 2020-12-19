"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
median of the two sorted arrays.
"""
import sys
from typing import List


class Solution:
    def is_partition_correct(self, l1: List[int], l2: List[int], mid_l1: int, mid_l2: int):
        """
        Partition is correct if it splits lists such that max element of the left
        side of one array is smaller or equal to the min element to the right side of
        the other array
        """
        max_left_l1 = -sys.maxsize if mid_l1 == 0 else l1[mid_l1 - 1]
        max_left_l2 = -sys.maxsize if mid_l2 == 0 else l2[mid_l2 - 1]
        min_right_l1 = sys.maxsize if mid_l1 == len(l1) else l1[mid_l1]
        min_right_l2 = sys.maxsize if mid_l2 == len(l2) else l2[mid_l2]
        if max_left_l1 <= min_right_l2 and max_left_l2 <= min_right_l1:
            return True
        else:
            return False

    def find_median(self, l1: List[int], l2: List[int], mid_l1: int, mid_l2: int):
        max_left_l1 = -sys.maxsize if mid_l1 == 0 else l1[mid_l1 - 1]
        max_left_l2 = -sys.maxsize if mid_l2 == 0 else l2[mid_l2 - 1]
        min_right_l1 = sys.maxsize if mid_l1 == len(l1) else l1[mid_l1]
        min_right_l2 = sys.maxsize if mid_l2 == len(l2) else l2[mid_l2]

        if (len(l1) + len(l2)) % 2 == 0:
            return 0.5 * (
                    min(min_right_l1, min_right_l2) + max(max_left_l1, max_left_l2)
            )
        else:
            # We've ensured that any partition will lead to number of elements
            #  in LHS == RHS or LHS > RHS (by 1) in which case the median is on the LHS
            return max(max_left_l1, max_left_l2)

    def find_partition_idxs(self, l1: List[int], l2: List[int], start: int, end: int):
        """
        Partition at idx `i` means "before" elem at index i (otherwise we're unable to
        partition before the first element
        """
        total_elems = len(l1) + len(l2)
        mid_l1 = (start + end) // 2  # => num elements in LHS of l1
        mid_l2 = (total_elems + 1) // 2 - mid_l1
        return mid_l1, mid_l2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        # l1 is smaller than l2
        l1 = nums1 if m <= n else nums2
        l2 = nums1 if m > n else nums2
        start = 0
        end = len(l1)
        mid_l1, mid_l2 = self.find_partition_idxs(l1, l2, start, end)
        while True:
            max_left_l1 = -sys.maxsize if mid_l1 == 0 else l1[mid_l1 - 1]
            min_right_l2 = sys.maxsize if mid_l2 == len(l2) else l2[mid_l2]
            if self.is_partition_correct(l1, l2, mid_l1, mid_l2):
                return self.find_median(l1, l2, mid_l1, mid_l2)
            else:
                if max_left_l1 > min_right_l2:
                    end = mid_l1 - 1
                else:
                    # max left l2  > min right l1
                    start = mid_l1 + 1
                mid_l1, mid_l2 = self.find_partition_idxs(l1, l2, start, end)



s = Solution()

l1 = [6, 8]
l2 = [1, 2, 5, 7]
assert s.findMedianSortedArrays(l1, l2) == 5.5

l3 = [1, 2, 5, 7]
l4 = [6, 8, 9]
assert s.findMedianSortedArrays(l3, l4) == 6

l5 = [1, 2]
l6 = [3, 4]
assert s.findMedianSortedArrays(l5, l6) == 2.5

l7 = [1, 5, 6, 7]
l8 = [2, 3, 4, 8]
assert s.findMedianSortedArrays(l7, l8) == 4.5
