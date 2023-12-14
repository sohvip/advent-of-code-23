def tilt_the_rocks():
    platform = []
    with open('puzzle_input.txt', 'r') as file:
        for line in file:
            platform.append(list(line.strip()))
    for i in range(1, len(platform)):
        for j in range(len(platform[i])):
            if platform[i][j] == 'O':
                platform[i][j] = '.'
                index = i - 1
                while index >= 0:
                    if platform[index][j] == 'O' or platform[index][j] == '#':
                        platform[index + 1][j] = 'O'
                        break
                    index -= 1
                else:
                    platform[0][j] = 'O'
    total_load = 0
    load_amount = len(platform)
    for row in platform:
        for cell in row:
            if cell == 'O':
                total_load += load_amount
        load_amount -= 1             
    return total_load
