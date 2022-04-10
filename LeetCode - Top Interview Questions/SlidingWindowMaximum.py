from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def update_queue(queue: List[int], lookup: List[int], idx: int):
            # Maintain non-increasing queue
            while queue and lookup[queue[-1]] < lookup[idx]: 
                queue.pop()
            queue.append(idx)
        deque_ = deque()
        res = []
        for i in range(k):
            update_queue(deque_, nums, i)
        res.append(nums[deque_[0]])
        for i in range(k, len(nums)):
            update_queue(deque_, nums, i)
            if deque_[0] < i - (k - 1):
                deque_.popleft()
            res.append(nums[deque_[0]])
        return res
        

sol = Solution()
nums = [1,3,1,2,0,5]
k = 3
print(
    sol.maxSlidingWindow(nums, k)
)