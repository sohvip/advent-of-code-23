def mountain_mirrors():
    with open('puzzle_input.txt', 'r') as file:
        separate_patterns = file.read().split('\n\n')
        patterns = [line.split('\n') for line in separate_patterns]
    sum_of_notes = 0
    for pattern in patterns:
        mirror = False
        for index in range(len(pattern)):
            reflection = index + 1
            for i in range(index, -1, -1):
                if reflection >= len(pattern):
                    break
                if pattern[i] == pattern[reflection]:
                    mirror = True
                else:
                    mirror = False
                    break
                reflection += 1
            if mirror:
                sum_of_notes += 100 * (index + 1)
                break
        if not mirror:
            swapped_pattern = list(map(list, zip(*pattern)))
            for index in range(len(swapped_pattern)):
                reflection = index + 1
                for i in range(index, -1, -1):
                    if reflection >= len(swapped_pattern):
                        break
                    if swapped_pattern[i] == swapped_pattern[reflection]:
                        mirror = True
                    else:
                        mirror = False
                        break
                    reflection += 1
                if mirror:
                    sum_of_notes += index + 1
                    break     
    return sum_of_notes
