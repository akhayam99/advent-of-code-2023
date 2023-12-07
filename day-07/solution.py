import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

lines = getLinesFromFile('day-07')

myMap = {
    'high-card': [],
    'one-pair': [],
    'two-pair': [],
    'three-of-a-kind': [],
    'full-house': [],
    'four-of-a-kind': [],
    'five-of-a-kind': [],
}

hands = []
for line in lines:
    hand, points = line.replace('\n', '').split(' ')
    hands.append(hand + '$' + points)

def hand_strength(hand):
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    value = hand.split('$')[0]
    return [card_values[card] for card in value]

sortedHands = sorted(hands, key = hand_strength)

for item in sortedHands:
    hand, points = item.split('$')

    cards = re.compile(r'\w').findall(hand)
    occurrencens = []
    for card in list(set(cards)):
        occurrencens.append({card: hand.count(card)})

    sortedOccurrences = sorted(occurrencens, key=lambda x: list(x.values())[0], reverse=True)
    for index, sortedOccurrencesItem in enumerate(sortedOccurrences):
        card, occurrence = list(sortedOccurrencesItem.items())[0]
        if occurrence == 5:
            myMap['five-of-a-kind'].append(item); break
        if occurrence == 4:
            myMap['four-of-a-kind'].append(item); break
        if occurrence == 3:
            if sortedOccurrences[index + 1][list(sortedOccurrences[index + 1].keys())[0]] == 2:
                myMap['full-house'].append(item)
            else:
                myMap['three-of-a-kind'].append(item)
            break
        if occurrence == 2:
            if sortedOccurrences[index + 1][list(sortedOccurrences[index + 1].keys())[0]] == 2:
                myMap['two-pair'].append(item)
            else:
                myMap['one-pair'].append(item)
            break
        if occurrence == 1:
            myMap['high-card'].append(item); break

result, index = 0, 1
for key, value in myMap.items():
    for item in value:
        result += int(item.split('$')[1]) * index
        index += 1

print(result)

# Answer: 250370104
