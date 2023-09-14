import copy
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def solve(i: int, j: int, candidate: List[int]):
            nonlocal res, n, k
            if len(candidate) == k:
                res.append(candidate)
                return
            if i > n: return
            else:
                solve(i + 1, k - 1, candidate + [i])
                solve(i + 1, k - 1, candidate)
        solve(1, k, [])
        return res

n = 4
k = 1
s = Solution()
print(
    s.combine(n, k)
)
