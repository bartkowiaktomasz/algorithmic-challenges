from typing import List
from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        max_area = heights[0]
        # Insert an element of height 0 to pop all elements from the stack
        #  at the end
        heights.append(0)
        for i in range(len(heights)):
            if not stack:
                stack.append(i)
            else:
                # We're guaranteed that bar to the left of stack[-1] is smaller
                while stack and heights[stack[-1]] >= heights[i]:
                    popped_idx = stack.pop()
                    left_bound_bar_idx= stack[-1] if stack else -1
                    area = heights[popped_idx] * (i - left_bound_bar_idx - 1)
                    max_area = max(max_area, area)
                stack.append(i)
        return max_area


sol = Solution()
l = [4,3,4,5]
print(sol.largestRectangleArea(l))
