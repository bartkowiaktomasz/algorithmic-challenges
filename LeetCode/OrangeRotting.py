from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh = 0
        rotten_queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    rotten_queue.appendleft((i, j))
        if num_fresh == 0:
            return 0
        num_fresh_remaining = num_fresh
        minutes_cnt = 0
        new_rotten_queue = deque()
        while rotten_queue:
            if num_fresh_remaining == 0:
                if new_rotten_queue: return minutes_cnt + 1
                else: return minutes_cnt
            rotten = rotten_queue.pop()
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if di == 0 and dj == 0:
                    pass
                else:
                    i, j = rotten[0] + di, rotten[1] + dj
                    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                        if grid[i][j] == 1:
                            grid[i][j] = 2
                            new_rotten_queue.appendleft((i, j))
                            num_fresh_remaining += -1
            if not rotten_queue:
                rotten_queue, new_rotten_queue = new_rotten_queue, deque()
                minutes_cnt += 1
        return minutes_cnt if num_fresh_remaining == 0 else -1

sol = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[2,1,1],[0,1,1],[1,0,1]]
grid3 = [[0,2]]
grid4 = [[2,1,1],[1,1,1],[0,1,2]]
print(
    sol.orangesRotting(grid)
)