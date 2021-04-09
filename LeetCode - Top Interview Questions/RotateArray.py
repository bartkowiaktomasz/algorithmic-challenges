from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_seen, idx_start, n = 0, 0, len(nums)
        while nums_seen < n:
            idx = None
            while idx != idx_start:
                if idx is None:
                    idx = idx_start
                    elem = nums[idx]
                nums_seen += 1
                dest_idx = (idx + k) % n
                temp = nums[dest_idx]
                nums[dest_idx] = elem
                
                idx = dest_idx
                elem = temp
            idx_start += 1

sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
sol.rotate(nums, k)
print(nums)
        