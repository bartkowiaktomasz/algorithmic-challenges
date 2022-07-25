"""
Given `n` non-negative integers representing an elevation map where the width of each
bar is `1`, compute how much water it can trap after raining.
"""

from collections import deque
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        bottom_height, vol = 0, 0
        for i in range(len(height)):
            while stack:
                smaller_height = min(height[stack[-1]], height[i])
                vol += (
                    smaller_height - bottom_height
                ) * (i - stack[-1] - 1)
                bottom_height = smaller_height
                if height[i] < height[stack[-1]]:
                    # If current bar is smaller than the top in the stack
                    # Don't pop the top element
                    break
                stack.pop()
            stack.append(i)
        return vol


sol = Solution()
height = [4,2,0,3,2,5]
print(sol.trap(height))
