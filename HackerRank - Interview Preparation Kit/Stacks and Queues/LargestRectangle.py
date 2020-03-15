"""
Maximise a rectangular area under the histogram.
"""

import os
from collections import deque


# Complete the largestRectangle function below.
def largestRectangle(h):
    """
    Append zero height building for an algorithm not to fail after a
    strictly increasing sequence of buildings (it appends
    heights to the stack)
    """
    h.append(-1)
    stack = deque()
    max_area = h[0]
    for i, height in enumerate(h):
        if not stack or (stack and height >= h[stack[-1]]):
            stack.append(i)
        elif stack and height < h[stack[-1]]:
            while stack and h[stack[-1]] > height:
                current = stack.pop()
                if not stack:
                    current_area = h[current] * i
                else:
                    current_area = h[current] * (i - stack[-1] - 1)
                max_area = current_area if current_area > max_area else max_area
            stack.append(i)

    return max_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    h = list(map(int, input().rstrip().split()))
    result = largestRectangle(h)
    fptr.write(str(result) + '\n')
    fptr.close()
