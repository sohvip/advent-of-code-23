def solve_calibration_values():
    calibration_values = []
    with open('puzzle_input.txt', 'r') as document:
        for line in document:
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break
            value = first_digit + last_digit
            calibration_values.append(int(value))
    return sum(calibration_values)
