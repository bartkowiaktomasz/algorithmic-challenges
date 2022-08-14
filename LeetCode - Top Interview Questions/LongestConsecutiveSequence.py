from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        for n in nums:
            nums_set.add(n)
        longest = 0
        for n in nums:
            if n - 1 not in nums_set:
                cur_seq_length = 0
                i = n
                while i in nums_set:
                    cur_seq_length += 1
                    i += 1
                longest = max(longest, cur_seq_length)
        return longest

s = Solution()
nums = [1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3]
print(
    s.longestConsecutive(nums)
)