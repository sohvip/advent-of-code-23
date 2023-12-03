def possible_games():
    possible_game_ids = []
    with open('puzzle_input.txt', 'r') as games:
        for game in games:
            possible = True
            initial_split = game.split(': ')
            game_id = initial_split[0].split(' ')[1]
            sets = initial_split[1].split('; ')
            for s in sets:
                cubes = s.split(', ')
                for c in cubes:
                    amount = int(c.split(' ')[0])
                    if 'red' in c:
                        if amount > 12:
                            possible = False
                    elif 'green' in c:
                        if amount > 13:
                            possible = False
                    elif 'blue' in c:
                        if amount > 14:
                            possible = False
            if possible:
                possible_game_ids.append(int(game_id))
        return sum(possible_game_ids)
