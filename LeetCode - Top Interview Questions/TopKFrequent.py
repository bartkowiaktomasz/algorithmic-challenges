import heapq
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for n, count in counter.items():
            heapq.heappush(heap, (count, n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [tup[1] for tup in heap]

nums = [1,1,1,2,2,3]
k = 2
sol = Solution()
print(
    sol.topKFrequent(nums, k)
)