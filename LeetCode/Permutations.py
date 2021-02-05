"""
Given an array `nums` of distinct integers, return all the possible permutations. 
You can return the answer in any order.
"""

import copy
from typing import List


class Solution:
    def permuteRec(self, nums, single_res, res):
        if len(nums) == 1:
            last_elem = nums.pop()
            single_res.append(last_elem)
            res.append(single_res)
        else:
            for n in nums:
                nums_cp = copy.copy(nums)
                single_res_cp = copy.copy(single_res)
                nums_cp.remove(n)
                single_res_cp.append(n)
                self.permuteRec(nums_cp, single_res_cp, res)

    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = set(nums)
        res = []
        self.permuteRec(nums, [], res)
        return res


sol = Solution()
l = [1, 2, 3]
print(
    sol.permute(l)
)
