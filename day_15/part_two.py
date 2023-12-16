def lens_boxes():
    boxes = [[] for _ in range(256)]
    with open('puzzle_input.txt', 'r') as file:
        for line in file:
            strings = line.strip().split(',')
    box_number = 0
    label = ''
    for string in strings:
        for index, char in enumerate(string):
            if char.isalpha():
                box_number += ord(char)
                box_number *= 17
                box_number %= 256
                label += char
            elif char == '-':
                boxes[box_number] = [lens for lens in boxes[box_number] if lens[0] != label]
            elif char == '=':
                if any(lens[0] == label for lens in boxes[box_number]):
                    boxes[box_number] = [(label, int(string[index + 1:])) if lens[0] == label else lens for lens in boxes[box_number]]
                else:
                    boxes[box_number].append((label, int(string[index + 1:])))
        label = ''
        box_number = 0
    total_focusing_power = 0
    for index, box in enumerate(boxes):
        if len(box) > 0:
            for index_2, lens in enumerate(box):
                current_focusing_power = (index + 1) * (index_2 + 1) * lens[1]
                total_focusing_power += current_focusing_power
    return total_focusing_power
