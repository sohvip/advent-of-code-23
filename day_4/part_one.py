def points():
    total_points = 0
    with open('puzzle_input.txt', 'r') as file:
        for line in file:
            points = 0
            initial_split = line.split(': ')
            my_numbers = initial_split[1].split(' | ')[0].split(' ')
            winning_numbers = initial_split[1].split(' | ')[1].replace('\n', '').split(' ')
            for number in my_numbers:
                if number == '':
                    continue
                elif number in winning_numbers:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2
            total_points += points
        return total_points
