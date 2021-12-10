import math
import numpy as np
from queue import Queue

def lowPoint(candidate, grid):
    candidate_row = candidate[0]
    candidate_col = candidate[1]

    candidate = grid[candidate_row][candidate_col]

    if grid[candidate_row - 1][candidate_col] <= candidate:
        return False
    elif grid[candidate_row + 1][candidate_col] <= candidate:
        return False
    elif grid[candidate_row][candidate_col - 1] <= candidate:
        return False
    elif grid[candidate_row][candidate_col + 1] <= candidate:
        return False
    
    return True;

def part1(grid):
    low_points = []

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if lowPoint((i,j), grid):
                low_points.append((i,j))

    return low_points

def riskLevels(grid, low_points):
    low_points = [grid[point[0]][point[1]] + 1 for point in low_points]
    return sum(low_points)

def bfs(grid, point):
    search = Queue()
    search.put(point)

    basin_size = 0

    while not search.empty():
        active = search.get()
        row = active[0]
        col = active[1]

        if grid[row][col] != 9 and grid[row][col] != math.inf and grid[row][col] != -1:
            basin_size += 1
        else:
            continue
        
        grid[row][col] = -1

        if grid[row - 1][col] < 9 and grid[row - 1][col] != -1:
            search.put((row - 1, col))

        if grid[row + 1][col] < 9 and grid[row + 1][col] != -1:
            search.put((row + 1, col))

        if grid[row][col - 1] < 9 and grid[row][col - 1] != -1:
            search.put((row, col - 1))

        if grid[row][col + 1] < 9 and grid[row][col + 1] != -1:
            search.put((row, col + 1))
    
    return basin_size

def part2(grid, low_points):
    basin_sizes = []
    for point in low_points:
        basin_sizes.append(bfs(grid, point))

    basin_sizes = sorted(basin_sizes)
    top_three = basin_sizes[-3:]
    return np.prod(top_three)

    
def main():
    infile = open("input.txt")
    grid = infile.readlines()
    grid = [list(map(int, list(row.rstrip('\n')))) for row in grid]

    # Pad edges of array with infinity to avoid bounds checking
    for row in grid:
        row.insert(0, math.inf)
        row.append(math.inf)
    pad = [math.inf for i in range(0, len(grid[0]))]
    grid.insert(0, pad)
    grid.append(pad)

    low_points = part1(grid)

    print(part2(grid, low_points))


if __name__ == "__main__":
    main()
