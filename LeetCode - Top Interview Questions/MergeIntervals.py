"""
Given an array of intervals where `intervals[i] = [starti, endi]`, merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_sorted = sorted(intervals, key=lambda e: e[0])
        prev = intervals_sorted[0]
        res = []
        for i in intervals_sorted[1:]:
            if i[1] <= prev[1]: continue
            elif i[0] <= prev[1]: prev[1] = i[1]
            else:
                res.append(prev)
                prev = i
        res.append(prev)
        return res


sol = Solution()
intervals = [[1, 4], [2, 3]]
print(sol.merge(intervals))

