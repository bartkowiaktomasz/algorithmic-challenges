import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Idea: Instead of keeping the product, keep a sum of logs
        Cases to consider:
            - Zero element (the answer will have everywhere zeros except one position)
            - Negative elements (need to keep track of the count of negative elements)
        """
        def _sign(n: int):
            if n % 2 == 0:
                return 1
            else:
                return -1
        num_zeros_seen = 0
        num_negatives = 0
        idx_of_zero = None
        sum_ = 0
        for i, n in enumerate(nums):
            if n < 0:
                num_negatives += 1
            if n == 0:
                idx_of_zero = i
                num_zeros_seen += 1
            else:
                sum_ += math.log(abs(n))
            if num_zeros_seen > 1:
                return [0] * len(nums)
        if idx_of_zero is not None:
            res = [0] * len(nums)
            res[idx_of_zero] = _sign(num_negatives) * round(math.pow(math.e, sum_))
        else:
            res = [
                (_sign(num_negatives) if n > 0 else _sign(num_negatives - 1)) * 
                round(math.pow(math.e, sum_ - math.log(abs(n)))) for n in nums
            ]
        return res

sol = Solution()
nums = [-1,1,1,-3,3]
print(
    sol.productExceptSelf(nums)
)