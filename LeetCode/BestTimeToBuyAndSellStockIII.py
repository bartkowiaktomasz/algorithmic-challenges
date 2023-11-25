"""
Solution to 123 (188) Best Time to Buy and Sell Stock III (IV)
Explanation:
1. Start with maxProfitWithoutOptimisation
2. Optimised solution is maxProfit
3. Fastest solution is using "State machine" approach
"""
from collections import defaultdict
import math
from typing import List


class Solution:
    def maxProfitWithoutOptimisation(self, prices: List[int]) -> int:
        """
        - dp[(k, i)] - max profit until and including day i with k transactions left
        - State: dp[(k, i)] = max(do_nothing, sell_now) where:
            do_nothing := dp[(k, i - 1)]
            sell_now = max([prices[i] - prices[j] + dp[(k - 1, j - 1)] for j in range(i)])
                i.e. max profit until day i is a max over all potential days we could have bought
                (0 <= j < i) plus the optimal profit just before that day

        Issue: We repeat j = 0, ..., i - 1 for each i (O(n^2))
        Observation: In the expression:
            prices[i] - prices[j] + dp[(k - 1, j - 1)]
            maximising that expression is equivalent to minimising:
            prices[j] - dp[(k - 1, j - 1)]
            for each i. And this term only needs to be recomputed once for each i
        """
        dp = defaultdict(int)  # (k, i) -> max profit until and including day i with k transactions left
        k = 2
        for t in range(1, k + 1):
            for i in range(1, len(prices)):
                do_nothing = dp[(t, i - 1)]
                sell_now = max([
                    prices[i] - prices[j] + dp[(t - 1, j - 1)]
                    for j in range(i)
                ])
                dp[(t, i)] = max(
                    do_nothing,  # Do not buy or sell
                    sell_now # Sell at day i
                )
        return dp[(k, len(prices) - 1)]
 
    def _maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(int)  # (k, i) -> max profit until and including day i with k transactions left
        k = 2
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

    def maxProfit(self, prices: List[int]) -> int:
        """
        State machine approach. The user, at each iteration could be in one of 4 states:
        0 - bought first transaction
        1 - sold first transaction
        2 - bought second transaction
        3 - sold second transaction
        At each iteration we simulate all four scenarios, knowing that the best case for
        state X at iteration i is either stay in state X or change the state by buying/selling
        from the previous best state.
        """
        s = [-math.inf, 0, -math.inf, 0]
        for p in prices:
            s[0] = max(s[0], -p)
            s[1] = max(s[1], s[0] + p)
            s[2] = max(s[2], s[1] - p)
            s[3] = max(s[3], s[2] + p)
        return s[3]

prices = [7,6,4,3,1]
s = Solution()
print(
    s.maxProfit(prices)
)