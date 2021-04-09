"""
Implement `pow(x, n)`, which calculates `x` raised to the power `n`
"""

from typing import Dict

class Solution:
    def myPowRec(self, x: float, n: int, memo: Dict[int, float]) -> float:
        if n in memo:
            return memo[n]
        elif n == 1:
            return x
        else:
            res = self.myPowRec(x, n // 2, memo) * self.myPowRec(x, n - n // 2, memo)
            memo[n] = res
            return res

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.myPowRec(x, -n, {})
        elif n == 0:
            return 1
        else:
            return self.myPowRec(x, n, {})


sol = Solution()
x = 2
n = -2

print(
    sol.myPow(x, n)
)