from collections import Counter
from typing import List
import itertools

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumsum, res = 0, 0
        cumsums_seen = Counter([cumsum])
        for num in nums:
            cumsum += num
            res += cumsums_seen[cumsum - k]
            cumsums_seen[cumsum] += 1
        return res

sol = Solution()

nums = [1,1,1]
k = 2

nums2 = [1, 2, 3]
k2 = 3

nums3 = [1]
k3 = 0

assert sol.subarraySum(nums, k) == 2
assert sol.subarraySum(nums2, k2) == 2
assert sol.subarraySum(nums3, k3) == 0