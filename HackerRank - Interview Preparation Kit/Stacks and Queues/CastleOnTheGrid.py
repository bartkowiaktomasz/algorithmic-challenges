"""
You are given a square grid with some cells open (.) and some blocked (X).
Your playing piece can move along any row or column until it reaches the edge
of the grid or a blocked cell. Given a grid, a start and an end position,
determine the number of moves it will take to get to the end position.
"""

import os
from collections import deque


def possible_fields(direction, grid, x, y):
    size = len(grid)
    fields = []
    currentX, currentY = x, y
    if direction == 'l':
        while currentY > 0 and grid[currentX][currentY - 1] != 'X':
            currentY += -1
            fields.append((currentX, currentY))
    elif direction == 'r':
        while currentY < size - 1 and grid[currentX][currentY + 1] != 'X':
            currentY += 1
            fields.append((currentX, currentY))
    elif direction == 'u':
        while currentX > 0 and grid[currentX - 1][currentY] != 'X':
            currentX += -1
            fields.append((currentX, currentY))
    else:
        while currentX < size - 1 and grid[currentX + 1][currentY] != 'X':
            currentX += 1
            fields.append((currentX, currentY))

    return fields


# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    directions = ['l', 'r', 'u', 'd']
    currentX, currentY = startX, startY
    queue = deque()
    queue.append((startX, startY))
    in_queue = {}
    in_queue[startX, startY] = True
    visited = {}
    distance = {}
    visited[(startX, startY)] = False
    distance[(startX, startY)] = 0
    while not (currentX == goalX and currentY == goalY):
        currentX, currentY = queue.popleft()
        del in_queue[currentX, currentY]
        if (currentX, currentY) not in visited or not visited[(currentX, currentY)]:
            visited[(currentX, currentY)] = True
            current_dist = distance[(currentX, currentY)]
            for direction in directions:
                possible_fields_given_dir = possible_fields(direction, grid,
                                                            currentX, currentY)
                for field in possible_fields_given_dir:
                    if field not in visited and field not in in_queue:
                        distance[field] = current_dist + 1
                        queue.append(field)
                        in_queue[field] = True
    return distance[(currentX, currentY)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    startXStartY = input().split()
    startX = int(startXStartY[0])
    startY = int(startXStartY[1])
    goalX = int(startXStartY[2])
    goalY = int(startXStartY[3])
    result = minimumMoves(grid, startX, startY, goalX, goalY)
    fptr.write(str(result) + '\n')
    fptr.close()
