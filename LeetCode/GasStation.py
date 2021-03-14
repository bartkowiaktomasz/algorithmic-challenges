from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        sum_ = 0
        min_sum = float('inf')
        min_sum_idx = -1
        for i in range(n):
            sum_ += gas[i] - cost[i]
            if sum_ <= min_sum:
                min_sum = sum_
                min_sum_idx = i
        if sum_ < 0:
            return -1
        return (min_sum_idx + 1) % n

sol = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(
    sol.canCompleteCircuit(gas, cost)
)