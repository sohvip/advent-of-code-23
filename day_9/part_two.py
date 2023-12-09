def analyze_oasis_report_reversed():
    sequences = []
    predictions = []
    with open('puzzle_input.txt', 'r') as file:
        for line in file:
            row = line.strip().split(' ')
            row.reverse()
            sequences.append(row)
    for sequence in sequences:
        memory = []
        values = []
        for index, number in enumerate(sequence[1:], start=1):
            values.append(int(number) - int(sequence[index-1]))
        while True:
            memory.append(values)
            if len(set(values)) == 1:
                break
            else:
                values = []
                for index_2, value in enumerate(memory[-1][1:], start=1):
                    values.append(int(value) - int(memory[-1][index_2-1]))
        memory.reverse()
        placeholders = [memory[0][-1]]
        for index_3, step in enumerate(memory[1:], start=1):
            next_step = placeholders[index_3-1] + step[-1]
            placeholders.append(next_step)
        predictions.append(int(sequence[-1]) + placeholders[-1])
    return sum(predictions)
