def minimum_set():
    power_of_sets = []
    with open('puzzle_input.txt', 'r') as games:
        for game in games:
            red = green = blue = 0
            initial_split = game.split(': ')
            sets = initial_split[1].split('; ')
            for s in sets:
                cubes = s.split(', ')
                for c in cubes:
                    amount = int(c.split(' ')[0])
                    if 'red' in c:
                        if amount > red:
                            red = amount
                    elif 'green' in c:
                        if amount > green:
                            green = amount
                    elif 'blue' in c:
                        if amount > blue:
                            blue = amount
            power_of_sets.append(red * green * blue)
        return sum(power_of_sets)
