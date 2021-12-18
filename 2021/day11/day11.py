import numpy as np

increment = np.pad(np.ones((10, 10)), pad_width=1, constant_values=0)

def flash(input):
    flashcount = 0

    while True:
        match = np.where((input > 9) & (input != -2))
        if len(match[0]) == 0 or len(match[1]) == 0:
            return flashcount
        else:
            flashcount += 1

        first = (match[0][0], match[1][0])

        row = first[0]
        col = first[1]

        input[row][col] = -2

        left = input[row - 1][col]
        right = input[row + 1][col]
        up = input[row][col - 1]
        down = input[row][col + 1]
        left_up = input[row - 1][col - 1]
        left_down = input[row - 1][col + 1]
        right_up = input[row + 1][col - 1]
        right_down = input[row + 1][col + 1]


        if left != -1 and left != -2: 
            input[row - 1][col] += 1

        if right != -1 and right != -2: 
            input[row + 1][col] += 1

        if up != -1 and up != -2: 
            input[row][col - 1] += 1

        if down != -1 and down != -2: 
            input[row][col + 1] += 1

        if left_up != -1 and left_up != -2:
            input[row - 1][col - 1] += 1

        if left_down != -1 and left_down != -2:
            input[row - 1][col + 1] += 1

        if right_up != -1 and right_up != -2:
            input[row + 1][col - 1] += 1

        if right_down != -1 and right_down != -2:
            input[row + 1][col + 1] += 1

def step(input):
    return input + increment

def resetFlashers(input):
    input[input == -2] = 0
    return input

def main():
    infile = open("input.txt")
    input = [list(line.rstrip('\n')) for line in infile.readlines()]
    input = [list(map(int, line)) for line in input]
    input = np.pad(np.asarray(input, dtype='int32'), pad_width=1, constant_values=-1)

    total_flashes = 0
    i = 0

    while True:
        input = step(input)
        flashes_this_step = flash(input)
        if (flashes_this_step == 100):
            print(f"Synchronized first at step: {i + 1}")
            break
        total_flashes += flashes_this_step
        input = resetFlashers(input)

        if i == 99:
            print("Flashes at round 100: " + str(total_flashes))
        i += 1

if __name__ == "__main__":
    main()
