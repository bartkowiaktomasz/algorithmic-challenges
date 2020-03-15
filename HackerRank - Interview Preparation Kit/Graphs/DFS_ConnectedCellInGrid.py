def computeRegion(grid, n, m, regionSize, row, column):
    for r in [row - 1, row, row + 1]:
        for c in [column - 1, column, column + 1]:
            if not (r < 0 or r >= n or c < 0 or c >= m):
                if (grid[r][c] != 0):
                    grid[r][c] = 0
                    regionSize[0] += 1
                    computeRegion(grid, n, m, regionSize, r, c)

    return regionSize[0]


def findLargestRegion(grid, n, m):
    grid_original = grid  # Copy grid and modify it while traversing
    largestRegion = 0
    for row in range(n):
        for column in range(m):
            if (grid[row][column] != 0):
                regionSize = [0]
                largestRegion = max(largestRegion, computeRegion(grid, n, m, regionSize, row, column))

    return largestRegion


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    print(findLargestRegion(grid, n, m))