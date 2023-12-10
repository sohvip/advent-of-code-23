def pipe_maze():
    pipe_map = [[] for _ in range(140)]
    with open('puzzle_input.txt', 'r') as file:
        for index, line in enumerate(file):
            clean_line = line.strip()
            for char in clean_line:
                pipe_map[index].append(char)
    point = [42, 24]
    steps = 0
    to = 'l'
    while True:
        steps += 1
        current = pipe_map[point[0]][point[1]]
        if current == 'S':
            break
        if (current == 'L' and to == 'l') or (current == 'J' and to == 'r'):
            point[0] -= 1
            to = 'u'
        elif (current == 'F' and to == 'l') or (current == '7' and to == 'r'):
            point[0] += 1
            to = 'd'
        elif (current == '7' and to == 'u') or (current == 'J' and to == 'd'):
            point[1] -= 1
            to = 'l'
        elif (current == 'F' and to == 'u') or (current == 'L' and to == 'd'):
            point[1] += 1
            to = 'r'
        elif current == '|' and to == 'u':
            point[0] -= 1
        elif current == '|' and to == 'd':
            point[0] += 1
        elif current == '-' and to == 'l':
            point[1] -= 1
        elif current == '-' and to == 'r':
            point[1] += 1      
    return steps // 2
