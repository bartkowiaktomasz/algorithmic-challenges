from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length_map = dict()
        max_length_seq = 0
        for e in nums:
            length_map[e] = 1
        for e in nums:
            length_seq = 1
            running = e
            if length_map[e] == 1:
                # Iterate through (greater) consecutive elements only if sequence
                #  length for current element is 1. This means that the element
                #  was not updated in one of previous iterations
                while running + 1 in length_map:
                    if length_map[running + 1] > 1:
                        length_map[running] = length_map[running + 1] + 1
                        length_seq = length_map[running]
                        break
                    length_seq += 1
                    running += 1
            # Come back from `running` to `e` and update all elements between
            #  them
            i = 1
            while running > e:
                if length_map[running - 1] == 1:
                    # Only update if it has not been yet updated
                    length_map[running - 1] = length_map[running] + 1
                running -= 1
                i += 1
            max_length_seq = max(max_length_seq, length_map[e])
            print(length_map)
        return max_length_seq

s = Solution()
nums = [1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3]
print(
    s.longestConsecutive(nums)
)