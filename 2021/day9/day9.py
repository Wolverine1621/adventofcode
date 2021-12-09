import math

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
    risk_levels = []

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if lowPoint((i,j), grid):
                risk_levels.append(grid[i][j] + 1)

    return sum(risk_levels)


    
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

    print(part1(grid))

if __name__ == "__main__":
    main()
