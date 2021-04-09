from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_n_to_idx = dict()
        for i, n in enumerate(nums):
            if target - n in map_n_to_idx:
                return [i, map_n_to_idx[target - n]]
            map_n_to_idx[n] = i


input = [2, 7, 11, 15]
target = 9

print(
    Solution().twoSum(input, target)
)
