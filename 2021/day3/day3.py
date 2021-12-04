import copy

def countFrequencies(input, index) -> (int, int): # (0, 1)
    zero_count = 0
    one_count = 0

    for num in input:
        if num[index] == '0':
            zero_count += 1
        elif num[index] == '1':
            one_count += 1
        else:
            print("... how?")

    return (zero_count, one_count)

def mostCommon(freqs):
    if (freqs[0] == freqs[1]):
        return -1

    return '0' if freqs[0] > freqs[1] else '1'

def leastCommon(freqs):
    if (freqs[0] == freqs[1]):
        return -1

    return '0' if freqs[0] < freqs[1] else '1'

def main():
    input = open("input.txt").readlines()
    input = [line.rstrip('\n') for line in input]

    gamma = ""
    epsilon = ""
    for i in range(0, len(input[0])):
        gamma += mostCommon(countFrequencies(input, i))
        epsilon += leastCommon(countFrequencies(input, i))

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(f"Gamma: {gamma}\nEpsilon: {epsilon}\nPower Consumption: {gamma * epsilon}")
    print("== PART 2 ==")

    oxy_set = input
    co2_set = copy.deepcopy(input)
    
    # OXYGEN FILTERING
    position = 0
    while len(oxy_set) > 1:
        criteria = mostCommon(countFrequencies(oxy_set, position))
        if (criteria == -1):
            criteria = 1

        oxy_set = [num for num in oxy_set if num[position] == str(criteria)]
        position += 1
    
    oxy = int(oxy_set[0], 2)

    # CO2 FILTERING
    position = 0
    while len(co2_set) > 1:
        criteria = leastCommon(countFrequencies(co2_set, position))
        if (criteria == -1):
            criteria = 0

        co2_set = [num for num in co2_set if num[position] == str(criteria)]
        position += 1

    co2 = int(co2_set[0], 2)

    print(f"Oxygen: {oxy}\nCO2: {co2}\nRating: {oxy * co2}")

if __name__ == "__main__":
    main()
