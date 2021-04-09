from typing import List
import functools

def compare(a: int, b: int):
    a_str, b_str = str(a), str(b)
    x = int(a_str + b_str)
    y = int(b_str + a_str)
    return x - y

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all([n == 0 for n in nums]):
            return "0"
        return "".join(
            list(map(str, 
            sorted(nums, key=functools.cmp_to_key(compare))[::-1]))
        )


nums = [0, 0]
sol = Solution()
print(
    sol.largestNumber(nums)
)