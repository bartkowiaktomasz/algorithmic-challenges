from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                # reset counting because we've seen as many "candidate" elements
                # as "non-candidate" elements
                candidate = num
            count += (1 if num == candidate else -1) 
        return candidate

sol = Solution()
nums = [3,2,3]
print(
    sol.majorityElement(nums)
)