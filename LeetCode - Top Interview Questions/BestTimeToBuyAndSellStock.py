from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for p in prices:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)
        return max_profit
    