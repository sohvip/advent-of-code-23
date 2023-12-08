from math import lcm
from functools import reduce

def ghost_map():
    with open('puzzle_input.txt', 'r') as file:
        lines = file.readlines()
        instructions = lines[0].strip()
        the_map = {}
        starting_points = []
        for i in range(2, len(lines)):
            node = lines[i].split(' = ')[0]
            if node[2] == 'A':
                starting_points.append(node)
            left = lines[i].split(' = ')[1][1:4]
            right = lines[i].split(' = ')[1][6:9]
            the_map[node] = (left, right)
    steps = 0
    while True:
        for i in instructions:
            steps += 1
            for index, point in enumerate(starting_points):
                if isinstance(starting_points[index], int):
                    continue
                if i == 'L':
                    starting_points[index] = the_map[point][0]
                else:
                    starting_points[index] = the_map[point][1]

                if starting_points[index][2] == 'Z':
                    
                    starting_points[index] = steps
            for j in starting_points:
                if isinstance(j, str):
                    break
            else:
                return reduce(lcm, starting_points)
