import numpy as np

def isOpener(char):
    if char == '{' or char == '(' or char == '[' or char == '<':
        return True
    else:
        return False

def checkMatching(opener, closer):
    match closer:
        case ')':
            return True if opener == '(' else False

        case '}':
            return True if opener == '{' else False

        case ']':
            return True if opener == '[' else False

        case '>':
            return True if opener == '<' else False
        

def checkLine(line):
    stack = []

    for char in line:
        if isOpener(char):
            stack.append(char)
        else:
            candidate = stack.pop()

            if not checkMatching(candidate, char):
                return char

    total_score = 0
    while len(stack) > 0:
        opener = stack.pop()
        total_score *= 5

        if opener == '(':
            total_score += 1
        elif opener == '[':
            total_score += 2
        elif opener == '{':
            total_score += 3
        elif opener == '<':
            total_score += 4

    return total_score

def score(char):
    if char == ')': return 3

    if char == ']': return 57

    if char == '}': return 1197

    if char == '>': return 25137

def main():
    fname = "input.txt"
    input = [line.rstrip("\n") for line in open(fname).readlines()]
    error_score = 0
    completion_scores = []

    for line in input:
        result = checkLine(line)
        if type(result) == type(')'):
            error_score += score(result)
        else:
            completion_scores.append(result)

    print(f"Error score: {error_score}")
    middle = int(np.median(sorted(completion_scores)))
    print(f"Middle completion score: {middle}")

if __name__ == "__main__":
    main()
