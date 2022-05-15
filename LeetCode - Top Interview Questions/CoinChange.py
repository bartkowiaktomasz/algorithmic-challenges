from typing import List
import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def _solve(amount: int):
            nonlocal coins
            if amount == 0:
                return 0
            if amount < 0:
                return
            if amount in dp:
                return dp[amount]
            min_ = sys.maxsize
            for coin in coins:
                res = _solve(amount - coin)
                if res is not None:
                    min_ = min(1 + res, min_)
            dp[amount] = min_
            return min_
        res = _solve(amount)
        return res if res != sys.maxsize else -1

sol = Solution()
coins = [1]
amount = 0
print(
    sol.coinChange(coins, amount)
)
        