from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = min(height[i], height[j]) * (j - i)
        while i != j:
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area


s = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(
    s.maxArea(height)
)
