def scratchcards():
    cards = []
    with open('puzzle_input.txt', 'r') as file:
        for line in file:
            initial_split = line.split(': ')
            my_numbers = initial_split[1].split(' | ')[0].split(' ')
            winning_numbers = initial_split[1].split(' | ')[1].replace('\n', '').split(' ')
            cards.append([1, my_numbers, winning_numbers])
    total_cards = len(cards)
    for index, card in enumerate(cards):
        cards_won = 0
        factor = card[0]
        for number in card[1]:
            if number == '':
                continue
            elif number in card[2]:
                cards_won += 1
        if cards_won > 0:
            for i in range(1, cards_won + 1):
                cards[index + i][0] += factor
            total_cards += factor * cards_won
    return total_cards
