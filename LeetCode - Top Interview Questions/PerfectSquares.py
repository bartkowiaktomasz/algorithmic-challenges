import math
import sys


class Solution:
    memo = {}
    def numSquares(self, n: int) -> int:
        def _numSquares(n: int):
            if n == 0:
                return 0
            if n in self.memo:
                return self.memo[n]
            upper = int(math.sqrt(n))
            min_ = sys.maxsize
            for i in range(upper, 0, -1):
                min_ = min(min_, _numSquares(n - i * i) + 1)
            self.memo[n] = min_
            return min_
        return _numSquares(n)
        
sol = Solution()
print(
    sol.numSquares(2021)
)