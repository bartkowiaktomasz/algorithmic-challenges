"""
Given `n` non-negative integers representing an elevation map where the width of each
bar is `1`, compute how much water it can trap after raining.
"""

from collections import deque
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = deque()
        res = 0
        for current_i, current_h in enumerate(height):
            if not stack or current_h <= height[stack[-1]]:
                stack.append(current_i)
            else:
                while stack and current_h > height[stack[-1]]:
                    # Pop element `e` from the top of the stack cause its smaller than
                    #  the current height
                    # Note: We will also use the element "before" that element (i.e.
                    #  next stack-top after popping `e`) to decide side used to
                    #  calculate volume
                    i = stack.pop()
                    if stack:
                        # Popped element provides horizontal lower bound for hight
                        # Horizontal upper bound is deinfed by smaller of two boundary
                        #  heights
                        side_height = min(current_h, height[stack[-1]]) - height[i]
                        volume = side_height * (current_i - stack[-1] - 1)
                        res += volume
                stack.append(current_i)
        return res


sol = Solution()
height = [4,2,0,3,2,5]
print(sol.trap(height))
