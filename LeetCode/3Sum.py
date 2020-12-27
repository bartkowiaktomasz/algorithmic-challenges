from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            # Optimisation 1
            if i > 0 and nums[i] == nums[i - 1]:
                # If nums[i] == nums[i - 1] then we're gonna find the same l, r
                #  and so the answer found will be the same
                continue
            # Optimisation 2
            if nums[i] > 0:
                # List is sorted so if nums[i] > 0 then nums[l] > 0 and nums[r] > 0
                #  So the sum cannot be 0
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    # sum > 0
                    r -= 1
        return res


s = Solution()
nums_l = [
    [-1, 0, 1, 2, -1, -4], [], [0], [-1,0,1,2,-1,-4], [0,0,0,0]
]
nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
# print(
#     [s.threeSum(nums) for nums in nums_l]
# )
print(s.threeSum(nums))
