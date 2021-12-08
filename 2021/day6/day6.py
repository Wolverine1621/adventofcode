import copy

def simulatePopulation(initial_condition, days):
    school = [0 for i in range(0, 9)]

    for age in initial_condition:
        school[age] += 1

    for day in range(0, days):
        num_spawning = 0
        next_day = [0 for i in range(0,9)]

        for i in range(0, 8):
            if i == 0:
                next_day[0] = 0 + school[1]
                num_spawning = school[0]
                next_day[6] += num_spawning
                next_day[8] += num_spawning
            else:
                next_day[i] += school[i + 1]

        school = copy.deepcopy(next_day)

    return sum(school)

            


def main():
    fname = "input.txt"
    initial_condition = open(fname).read().rstrip('\n').split(',')
    initial_condition = [int(fish) for fish in initial_condition]
    eighty = simulatePopulation(initial_condition, 80)
    twofiftysix = simulatePopulation(initial_condition, 256)
    print(f"80 DAYS: {eighty}\n256 DAYS: {twofiftysix}")

if __name__ == "__main__":
    main()
