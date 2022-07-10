from typing import List
import copy
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums_original = copy.copy(nums)
        self.nums = nums

    def reset(self) -> List[int]:
        self.nums = copy.copy(self.nums_original)
        return self.nums

    def shuffle(self) -> List[int]:
        i = 0
        while i < len(self.nums):
            idx = random.randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[idx] = self.nums[idx], self.nums[i]
            i += 1
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()