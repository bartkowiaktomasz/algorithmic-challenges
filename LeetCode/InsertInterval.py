from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        left, right = [], []
        start, end = newInterval[0], newInterval[1]
        for i in intervals:
            if i[1] < newInterval[0]: left.append(i)
            elif i[0] > newInterval[1]: right.append(i)
            else:
                start = min(i[0], start)
                end = max(i[1], end)
        return left + [[start, end]] + right

intervals = [[1,3],[6,9]]; newInterval = [0,6]
sol = Solution()
print(
    sol.insert(intervals, newInterval)
)