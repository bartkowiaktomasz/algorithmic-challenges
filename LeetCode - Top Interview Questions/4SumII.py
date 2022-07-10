from collections import Counter
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_ = Counter(a + b for a in nums1 for b in nums2)
        sum_2 = Counter(c + d for c in nums3 for d in nums4)
        return sum(cnt * sum_2[-val] for val, cnt in sum_.items())

sol = Solution()
print(
    sol.fourSumCount(nums1 = [-1, -1], nums2 = [-1, 1], nums3 = [-1, 1], nums4 = [1, -1])
)
