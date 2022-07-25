from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def solve(candidates: List[int], cur: List[int], target: int):
            nonlocal res
            if len(res) >= 150:
                raise OverflowError
            if target == 0:
                res.append(cur)
                return
            if not candidates:
                return
            if target < 0:
                return
            for i in range(len(candidates)):
                solve(candidates[i:], [candidates[i]] + cur, target - candidates[i])
        try:
            solve(candidates, [], target)
        except OverflowError:
            return res
        return res

sol = Solution()
candidates = [2,3,5]
target = 8
print(
    sol.combinationSum(candidates, target)
)