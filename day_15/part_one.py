def hash_algorithm():
    with open('puzzle_input.txt', 'r') as file:
        for line in file:
            strings = line.strip().split(',')
    current_value = 0
    sum_of_values = 0
    for string in strings:
        for char in string:
            current_value += ord(char)
            current_value *= 17
            current_value %= 256
        sum_of_values += current_value
        current_value = 0
    return sum_of_values
