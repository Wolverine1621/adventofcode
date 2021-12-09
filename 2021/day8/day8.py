def count1478(input_right):
    sum = 0

    for line in input_right:
        targets = [code for code in line if len(code) == 2 or len(code) == 3 or len(code) == 4 or len(code) == 7]
        sum += len(targets)

    return sum

def part2(input_left, input_right):
    total = 0

    for i in range(0, len(input_left)):
        ones = [code for code in input_left[i] if len(code) == 2]
        fours = [code for code in input_left[i] if len(code) == 4]
        one_set = set(ones[0])
        four_set = set(fours[0])
        l_shape = four_set.difference(one_set)
        
        line_output = ""
        for display in input_right[i]:
            display_set = set(display)
            digit = -1

            if len(display) == 2: # one
                digit = 1

            elif len(display) == 3: # seven
                digit = 7

            elif len(display) == 4: # four
                digit = 4

            elif len(display) == 5: # two, three, or 5
                if len(display_set.intersection(l_shape)) == 2:
                    digit = 5
                elif len(display_set.intersection(one_set)) == 2:
                    digit = 3
                else:
                    digit = 2

            elif len(display) == 6: # 0, 6, or 9
                if len(display_set.intersection(l_shape)) == 2 and len(display_set.intersection(one_set)) == 2:
                    digit = 9
                elif len(display_set.intersection(l_shape)) == 2:
                    digit = 6
                else:
                    digit = 0

            elif len(display) == 7: # 8
                digit = 8

            line_output += str(digit)

        total += int(line_output)

    return total
                
def main():
    infile = open("input.txt")
    input_lines = infile.readlines()
    input_lines = [line.rstrip('\n') for line in input_lines]
    input_left = [line[:line.index('|')].split() for line in input_lines]
    input_right = [line[line.index('|') + 1:].split() for line in input_lines]

    print("1s, 4s, 7s, 8s: " + str(count1478(input_right)))
    print("Outputs totaled: " + str(part2(input_left, input_right)))


if __name__ == "__main__":
    main()
