def dive(infile, mode):
    horizontal = 0
    depth = 0
    aim = 0

    while True:
        input_ln = infile.readline().rstrip('\n').split()
        if not input_ln: break

        val = int(input_ln[1])
        match input_ln[0]:
            case "forward":
                horizontal += val 

                if mode == 2:
                    depth += (aim * val)


            case "down":
                if mode == 1:
                    depth += val
                elif mode == 2:
                    aim += val
                else:
                    print("Command error")

            case "up":
                if mode == 1:
                    depth -= val
                if mode == 2:
                    aim -= val

            case _:
                print("Error!")

    print(f"Horizontal: {horizontal}\nDepth: {depth}\nProduct: {horizontal * depth}")

def main():
    infile = open("input.txt")
    print("PART 1:")
    dive(infile, 1)

    print("\nPART 2:")
    infile.seek(0)
    dive(infile, 2)

if __name__ == "__main__":
    main()

