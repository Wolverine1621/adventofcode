from itertools import combinations

# Read input
input = open("input.txt", 'r')
input = input.read()
input = input.split()
input = list(map(int, input))

# Generate combinations
combos_2 = combinations(input, 2)

# Build results list
result_2 = [(x, y, x + y) for (x, y) in combos_2]


for combo in result_2:
    if combo[2] == 2020:
        print(f"Part 1: {combo[0] * combo[1]}")
        break;

# Part Two
combos_3 = combinations(input, 3)
result_3 = [(x, y, z, x + y + z) for (x, y, z) in combos_3]

for combo in result_3:
    if combo[3] == 2020:
        print(f"Part 2: {combo[0] * combo[1] * combo[2]}")
        break;
