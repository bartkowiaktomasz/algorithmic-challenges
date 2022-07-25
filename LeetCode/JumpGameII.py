import sys
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, dest = 0, len(nums) - 1
        while True:
            for i in range(dest + 1):
                if dest == 0:
                    return jumps
                if i + nums[i] >= dest:
                    jumps += 1
                    dest = i
                    break

sol = Solution()
print(
    sol.jump([2,3,0,1,4])
)