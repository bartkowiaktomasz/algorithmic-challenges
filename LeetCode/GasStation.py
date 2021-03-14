from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        delta = []
        for i in range(n):
            delta.append(gas[i] - cost[i])
        if sum(delta) < 0:
            return -1
        sum_gas, idx, start_idx = 0, 0, 0
        while idx < n:
            sum_gas += delta[idx]
            if sum_gas < 0:
                start_idx += 1
                idx, sum_gas = start_idx, 0
            else:
                idx += 1
        return start_idx

sol = Solution()
gas = [2,3,4]
cost = [3,4,3]
print(
    sol.canCompleteCircuit(gas, cost)
)