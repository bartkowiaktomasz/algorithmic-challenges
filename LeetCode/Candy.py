from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l, r = [1] * len(ratings), [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                l[i] = l[i - 1] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                r[i - 1] = r[i] + 1
        return sum([max(i, j) for i, j in zip(l, r)])

sol = Solution()
print(
    sol.candy([1,2,2])
)
