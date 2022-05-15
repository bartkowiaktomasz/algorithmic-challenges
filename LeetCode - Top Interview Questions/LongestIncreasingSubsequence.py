from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stacks = [[nums[0]]]
        for n in nums[1:]:
            # Note: for...else
            # If break is encountered inside "for", else
            for s in stacks:
                if n <= s[-1]:
                    s.append(n)
                    break
            else:
                # there is no stack where we can
                # append our element - create a new 
                # (empty) one
                stacks.append([n])
        return len(stacks)

sol = Solution()
nums = [10,9,2,5,3,7,101,18]
print(
    sol.lengthOfLIS(nums)
)

                
                