import copy

def countPaths(map, start, visited, twice=False):
    visited = copy.deepcopy(visited)
    if start == "end":
        return 1

    if start.islower():
        visited.append(start)

    count = 0
    edges = map[start]
    for edge in edges:
        if edge in visited and twice and edge != "start":
            count += countPaths(map, edge, visited)
        elif edge not in visited:
            count += countPaths(map, edge, visited, twice)

    return count

def main():
    input = open("input.txt").readlines()
    input = [line.rstrip('\n').split('-') for line in input]
    
    map = {}
    for edge in input:
        if edge[0] not in map: 
            map[edge[0]] = [edge[1]]
        else:
            map[edge[0]].append(edge[1])

        if edge[1] not in map:
            map[edge[1]] = [edge[0]]
        else:
            map[edge[1]].append(edge[0])

    part_one = countPaths(map, "start", [])
    part_two = countPaths(map, "start", [], True)
    print(f"Part 1: {part_one}")
    print(f"Part 2: {part_two}")
    
if __name__ == "__main__":
    main()
