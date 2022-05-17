import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        tmp = math.log(n, 3) % 1
        return math.isclose(tmp, 0, rel_tol=10e-12) or math.isclose(tmp, 1, rel_tol=10e-12)

sol = Solution()
nums = [
    0, 3, 9, 27, 243, 900, 1162261466
]
true_nums = [3**x for x in range(20)]
print(
    [sol.isPowerOfThree(n) for n in nums]
)