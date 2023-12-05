file_path = "./2023/Day 4/input.txt"
with open(file_path) as file:
    lines = [line.rstrip() for line in file]
    
def get_my_card(line):
    my_cards = line.split('|')
    my_cards = my_cards[1].split(' ')
    my_cards = [card for card in my_cards if card != '']
    return my_cards

def get_winning_card(line):
    winning_cards = line.split('|')
    winning_cards = winning_cards[0].split(':')
    winning_cards = winning_cards[1].split(' ')
    winning_cards = [card for card in winning_cards if card != '']
    return winning_cards


all_winning_cards = []
all_my_cards = []
points = 0
i = 0

for line in lines:
    all_winning_cards.append(get_winning_card(line))
    all_my_cards.append(get_my_card(line))

for hand in all_my_cards:
    hand_points = 0
    for card in hand:
        if card in all_winning_cards[i]:
            if hand_points == 0:
                hand_points += 1
            else:
                hand_points = hand_points*2
    points += hand_points    
    i += 1
print(points)