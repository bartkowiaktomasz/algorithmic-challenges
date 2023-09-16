from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return triangle[0][0]
        for h in range(1, len(triangle)):
            for i in range(h + 1):  # There are (h + 1) elems at height h
                if i == 0: min_ = triangle[h - 1][i]
                elif 0 < i < h: min_ = min(triangle[h - 1][i - 1], triangle[h - 1][i])
                else: min_ = triangle[h - 1][i - 1]
                triangle[h][i] += min_
        return min(triangle[-1])

sol = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(
    sol.minimumTotal(triangle)
)