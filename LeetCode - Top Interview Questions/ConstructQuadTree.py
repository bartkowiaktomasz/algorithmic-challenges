from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        h, w = len(grid), len(grid[0])
        def _build(y1, y2, x1, x2):
            nonlocal grid
            if y2 == y1 + 1:  # single square
                return Node(grid[y1][x1] == 1, True, None, None, None, None)
            ym = y1 + (y2 - y1) // 2
            xm = x1 + (x2 - x1) // 2
            sub_squares = [_build(y1, ym, x1, xm), _build(y1, ym, xm, x2), _build(ym, y2, x1, xm), _build(ym, y2, xm, x2)]
            if all(s.val is True for s in sub_squares): return Node(True, True, None, None, None, None)
            if all(s.val is False and s.isLeaf is True for s in sub_squares): return Node(False, True, None, None, None, None)
            else: return Node(False, False, sub_squares[0], sub_squares[1], sub_squares[2], sub_squares[3])
        root = _build(0, h, 0, w)
        return root

sol = Solution()
# grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
grid = [[1,1,0,0],[0,0,1,1],[1,1,0,0],[0,0,1,1]]
print(
    sol.construct(grid)
)