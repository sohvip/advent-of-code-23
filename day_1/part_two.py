from word2number import w2n

def is_number(index, line):
    spelled = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    word = ''
    while index < len(line):
        word += line[index]
        if word in spelled:
            return word
        index += 1
    return None

def solve_calibration_values_2():
    calibration_values = []
    with open('puzzle_input.txt', 'r') as document:
        for line in document:
            for i in range(len(line)):
                if line[i].isdigit():
                    first_digit = line[i]
                    break
                word = is_number(i, line)
                if word is not None:
                    first_digit = str(w2n.word_to_num(word))
                    break
            for i in range(len(line)-1, -1, -1):
                if line[i].isdigit():
                    last_digit = line[i]
                    break
                word = is_number(i, line)
                if word is not None:
                    last_digit = str(w2n.word_to_num(word))
                    break
            value = first_digit + last_digit
            calibration_values.append(int(value))
    return sum(calibration_values)
