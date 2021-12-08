def transpose(lst):
    return [list(tuple) for tuple in zip(*lst)]

def updateBoard(call, board):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == call:
                board[i][j] = "X"

def checkWin(board):
    win = ["X", "X", "X", "X", "X"]
    return (win in board) or (win in transpose(board))

def sumBoard(board):
    total = 0

    for row in board:
        for string in row:
            if string != "X":
                total += int(string)

    return total

def countWinners(boards):
    total = 0
    for board in boards:
        if checkWin(board):
            total += 1

    return total

def notWon(boards):
    result = []
    for i in range(0, len(boards)):
        if not checkWin(boards[i]):
            result.append(i)

    return result

def part1(sequence, boards):
    for call in sequence:
        for i in range(0, len(boards)):
            updateBoard(call, boards[i])
            if (checkWin(boards[i])):
                print(sumBoard(boards[i]) * int(call))
                return

def part2(sequence, boards):
    while True:
        call = sequence[0]
        
        for i in range(0, len(boards)):
            candidates = notWon(boards)
            updateBoard(call, boards[i])

            if len(candidates) == 1 and checkWin(boards[candidates[0]]):
                print(sumBoard(boards[candidates[0]]) * int(call))
                return

        del sequence[0]

def main():
    infile = open("input.txt")
    sequence = infile.readline().rstrip('\n').split(',')
    dump_newline = infile.readline()
    input = infile.read().split('\n\n') # Separate boards
    input = [board.split('\n') for board in input] # Separate into rows
    input[-1].remove("") # Remove odd hanging empty string

    for i in range(0, len(input)): # Process into ints
        input[i] = [row.split() for row in input[i]]

    print("Part 1:", end="")
    part1(sequence, input)
    print("Part 2:", end="")
    part2(sequence, input)

    
if __name__ == "__main__":
    main()
