def use_the_map():
    with open('puzzle_input.txt', 'r') as file:
        lines = file.readlines()
        instructions = lines[0].strip()
        the_map = {}
        for i in range(2, len(lines)):
            node = lines[i].split(' = ')[0]
            left = lines[i].split(' = ')[1][1:4]
            right = lines[i].split(' = ')[1][6:9]
            the_map[node] = (left, right)
    steps = 0
    spot = 'AAA'
    while True:
        for i in instructions:
            steps += 1
            if i == 'L':
                spot = the_map[spot][0]
            else:
                spot = the_map[spot][1]
            if spot == 'ZZZ':
                return steps
