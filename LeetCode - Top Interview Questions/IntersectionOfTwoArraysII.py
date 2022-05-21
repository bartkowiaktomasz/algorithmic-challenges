from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        intersection = counter1 & counter2
        return [e for e in intersection.keys() for _ in range(intersection[e])]