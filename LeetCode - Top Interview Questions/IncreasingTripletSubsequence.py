from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stacks = [[nums[0]]]
        for n in nums[1:]:
            if len(stacks) == 3:
                return True
            for s in stacks:
                if n <= s[-1]:
                    s.append(n)
                    break
            else:
                stacks.append([n])
        return len(stacks) >= 3

sol = Solution()
nums = [1,2,3,4,5]
print(
    sol.increasingTriplet(nums)
)