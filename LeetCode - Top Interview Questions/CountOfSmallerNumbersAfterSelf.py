from typing import List
from collections import deque


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def _combine(left: List[int], right: List[int]):
            nonlocal nums
            nonlocal res
            combined = []
            i, j, num_elems_in_right_smaller_than_left = 0, 0, 0
            while i < len(left) or j < len(right):
                while (
                    (j < len(right) and i == len(left)) or (j < len(right) and i < len(left) and nums[right[j][0]] < nums[left[i][0]])
                ):
                    # Append elems from the right array to the merged arr, counting the number of them
                    num_elems_in_right_smaller_than_left += 1
                    combined.append(right[j])
                    j += 1
                while ((i < len(left)) and ((j == len(right)) or (nums[left[i][0]] <= nums[right[j][0]]))):
                    # Append elems from the left array to the result
                    # Increment the result counter for each of those elements by "num_elems_in_right_smaller_than_left"
                    res[left[i][0]] += num_elems_in_right_smaller_than_left
                    combined.append(left[i])
                    i += 1
            return combined

        def _mergeSort(tups: List[int]):
            if len(tups) > 1:
                mid = len(tups) // 2
                left = _mergeSort(tups[:mid])
                right = _mergeSort(tups[mid:])
                return _combine(left, right)
            else:
                return tups
        indices = [[i, 0] for i in range(len(nums))]
        res = [0] * len(nums)
        _mergeSort(indices)
        return res

sol = Solution()
nums_arr = [
    [5,2,6,1],
    [0, 2, 1],
    [0, 0],
    [0],
    [2, 0, 1],
    [1, 5, 0, 2]
]
for nums in nums_arr:
    print(
        sol.countSmaller(nums)
    )