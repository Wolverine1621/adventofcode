from collections import Counter

def drawLine(points):
    line = []

    start = points[0]
    end = points[1]
    if start[0] == end[0]: # Vertical
        x = start[0]
        y = start[1]

        if start[1] < end[1]: # Up
            while (x,y) != end:
                line.append((x,y))
                y += 1

        elif start[1] > end[1]: # Down
            while (x,y) != end:
                line.append((x,y))
                y -= 1
            

    elif start[1] == end[1]: # Horizontal
        x = start[0]
        y = start[1]

        if start[0] < end[0]: # Right
            while (x,y) != end:
                line.append((x,y))
                x += 1

        elif start[0] > end[0]: # Left
            while (x,y) != end:
                line.append((x,y))
                x -= 1

    else: # Diagonal
        x = start[0]
        y = start[1]

        if start[0] < end[0]: #Right
            if start[1] < end[1]: # Up
                while (x,y) != end:
                    line.append((x,y))
                    x += 1
                    y += 1

            elif start[1] > end[1]: # Down
                while(x,y) != end:
                    line.append((x,y))
                    x += 1
                    y -= 1

        elif start[0] > end[0]: # Left
            if start[1] < end[1]: # Up
                while (x,y) != end:
                    line.append((x,y))
                    x -= 1
                    y += 1

            elif start[1] > end[1]: # Down
                while (x,y) != end:
                    line.append((x,y))
                    x -= 1
                    y -= 1

    line.append(end)
    return line

def main():
    infile = open("input.txt")
    infile = infile.readlines()
    all_lines = []

    for row in infile:
        points = row.rstrip('\n').split(" -> ")
        start = (points[0][:points[0].index(',')], points[0][points[0].index(',') + 1:])
        start = (int(start[0]), int(start[1]))
        end = (points[1][:points[1].index(',')], points[1][points[1].index(',') + 1:])
        end = (int(end[0]), int(end[1]))
        
        line = drawLine([start, end])

        for point in line:
            all_lines.append(point)

    intersections = Counter(all_lines).values()
    intersections = [count for count in intersections if count > 1]
    print(len(intersections))


if __name__ == "__main__":
    main()
