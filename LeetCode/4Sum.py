from collections import defaultdict
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findTwoSum(nums: List[int], target: int) -> List[List[int]]:
            # Assumes `nums` is sorted
            i, j = 0, len(nums) - 1
            res = []
            while i < j:
                if i >= 1 and (nums[i] == nums[i - 1]):
                    i += 1
                    continue
                if j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j += -1
                    continue
                sum_ = nums[i] + nums[j] 
                if sum_ == target:
                    res.append([nums[i], nums[j]])
                    i += 1
                elif sum_ > target:
                    j += -1
                else:
                    i += 1
            return res

        def findNSum(nums, n, target):
            if n == 2:
                return findTwoSum(nums, target)
            else:
                res = []
                for i in range(len(nums)):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        sums_ = findNSum(nums[i + 1:], n - 1, target - nums[i])
                        for s in sums_:
                            # Insert nums[i] at the beginning
                            # faster than list concatenation
                            s.insert(0, nums[i])
                        res.extend(sums_)
                return res

        nums_sorted = sorted(nums)
        return findNSum(nums_sorted, 4, target)

sol = Solution()
nums = [1,0,-1,0,-2,2]
target = 0

nums = [2,2,2,2,2]
target = 8
print(
    sol.fourSum(nums, target)
)