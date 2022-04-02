"""
A city's skyline is the outer contour of the silhouette formed 
by all the buildings in that city when viewed from a distance.
Given the locations and heights of all the buildings, return
the skyline formed by these buildings collectively.

https://leetcode.com/problems/the-skyline-problem/
"""
from heapq import heapify, heappush, heappop
from collections import Sequence
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        1. Split buildings into single points and mark each point whether it is
            a left (l) or a right (r) point of a given building.
        2. Update the result if the max height o the priority queue changes 
            - skyline is formed by changing max heights
        3. Sort points based on three conditions:
            - X position
            - Type
            - Height
            (in this order). Left needs to be before Right (imagine what happens
            if there are two buildings same height, right side of first one overlaps 
            with the left side of the next one). Height-wise, if we have two left points 
            (same x), higher needs to be considered first. If two right points, consider
            the lower one first.
        """
        res = []
        buildings_heap = [0]
        points = []
        for b in buildings:
            points.append((b[0], b[2], -1)) # -1 : Left corner
            points.append((b[1], b[2], 1)) # 1: Right corner
        # Sort left-to-right and, if draw:
        # - Consider Left then Right
        # - If two left corners have the same "x", consider the higher one first
        # - If two right corners have the same "x", consider the lower one first
        # Trick: The last two conditions above can be met by sorting by (height * type_) 
        #  and having type -1 (left) and 1 (right)
        points_sorted = sorted(points, key=lambda p: (p[0], p[2],  p[2] * p[1]))
        for x, h, type_ in points_sorted:
            print(f"Processing element [{x}, {h} of type {type_}]], res: {res}, heap: {buildings_heap}")
            if type_ == -1:
                if not buildings_heap or h > -buildings_heap[0]:
                    res.append([x, h])
                heappush(buildings_heap, -h)
            else:
                prev_max_height = -buildings_heap[0]
                buildings_heap.remove(-h)
                heapify(buildings_heap)
                if -buildings_heap[0] < prev_max_height:
                    res.append([x, -buildings_heap[0]])
        return res


sol = Solution()
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
expected = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
res = sol.getSkyline(buildings)
print(res)
assert res == expected

buildings_2 = [[0,2,3],[2,5,3]]
expected_2 = [[0,3],[5,0]]
res_2 = sol.getSkyline(buildings_2)
print(res_2)
assert res_2 == expected_2