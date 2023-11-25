from collections import defaultdict
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = defaultdict(int)  # (k, i) -> max profit until and including day i with k transactions left
        for t in range(1, k + 1):
            diff = prices[0]
            for i in range(1, len(prices)):
                do_nothing = dp[(t, i - 1)]
                diff = min([
                    diff,
                    prices[i - 1] - dp[(t - 1, i - 2)]
                ])
                dp[(t, i)] = max(
                    do_nothing,  # Do not buy or sell
                    prices[i] - diff  # Sell at day i
                )
        return dp[(k, len(prices) - 1)]

sol = Solution()
k = 2; prices = [3,2,6,5,0,3]
print(
    sol.maxProfit(k, prices)
)