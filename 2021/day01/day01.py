import math

input = open("input.txt")
#input = open("testinput.txt")
input = input.read()
input = input.split()
input = list(map(int, input))


def part1(input):
    inc_count = 0
    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            inc_count += 1

    print(inc_count)

def sum_three(input, start):
    return input[start] + input[start + 1] + input[start + 2]

def part2(input):
    last_group_sum = sum_three(input, 0)


    inc_count = 0
    for i in range(2, len(input)):
        if i + 2 > (len(input) - 1):
            break;

        result = sum_three(input, i)
        if result > last_group_sum:
            inc_count += 1

        last_group_sum = result

    print(inc_count)

part2(input)
