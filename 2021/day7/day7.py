import numpy as np

def gauss(pos, target):
    dist = np.absolute(pos - target)

    return (dist * (dist + 1)) / 2

def fuelCost(pos, target, part):
    if part == 1:
        return np.absolute(pos - target)
    if part == 2:
        return int(gauss(pos, target))

def minCost(input, part):
    lower = np.min(input)
    upper = np.max(input)
    costs = []

    for target in range(lower, upper):
        total = 0
        for pos in input:
            total += fuelCost(pos, target, part)

        costs.append(total)

    return np.min(costs)

def main():
    input = [int(x) for x in open("input.txt").read().rstrip('\n').split(',')]
    part1 = minCost(input, 1)
    part2 = minCost(input, 2)

    print(f"Part 1: {part1}\nPart 2: {part2}")


if __name__ == "__main__":
    main()
