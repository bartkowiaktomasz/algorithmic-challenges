"""
Given an array of intervals where `intervals[i] = [starti, endi]`, merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda e: e[0])
        res = []
        left_bound = intervals[0][0]
        right_bound = intervals[0][1]
        for i in range(len(intervals) - 1):
            if (
                intervals[i + 1][0] <= right_bound
                and intervals[i + 1][1] <= right_bound
            ):
                continue
            if intervals[i + 1][0] <= right_bound:
                right_bound = intervals[i + 1][1]
            else:
                res.append([left_bound, right_bound])
                left_bound = intervals[i + 1][0]
                right_bound = intervals[i + 1][1]
        res.append([left_bound, right_bound])
        return res


sol = Solution()
intervals = [[1, 4], [2, 3]]
print(sol.merge(intervals))

