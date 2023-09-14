import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects_sorted = sorted(zip(profits, capital), key=lambda e: e[1])
        heap = []
        i = 0
        while k > 0:
            while i < len(projects_sorted) and projects_sorted[i][1] <= w:
                heapq.heappush(heap, (-projects_sorted[i][0], projects_sorted[i][1]))
                i += 1
            if heap: w += -heapq.heappop(heap)[0]
            else: return w
            k += -1
        return w
        

profits = [1,2,3]
capital = [1,1,2]
w = 0
k = 1

s = Solution()
print(
    s.findMaximizedCapital(k, w, profits, capital)
)