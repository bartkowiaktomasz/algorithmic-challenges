from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res

sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]
temperatures3 = [30,60,90]

print(
    sol.dailyTemperatures(temperatures3)
)
