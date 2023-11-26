from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_ = {}  # number -> latest index
        for i, n in enumerate(nums):
            if n in map_ and i - map_[n] <= k: return True
            else: map_[n] = i
        return False
        