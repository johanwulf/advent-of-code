from collections import Counter

input = open("input", "r")
ll = [x for x in input.read().strip().split("\n")]


def get_ranking(hand, p2):
    if p2:
        l = list(filter(lambda x: x != 1, hand))
        most_freq = 1

        if len(l) > 0:
            most_freq = Counter(l).most_common()[0][0]

        if 1 in hand:
            new = [x for x in hand]
            for i in range(len(hand)):
                if hand[i] == 1:
                    new[i] = most_freq
                else:
                    new[i] = hand[i]

            hand = tuple(new)

    cards = sorted(Counter(hand).values())

    if cards == [5]:
        return 7
    elif cards == [1, 4]:
        return 6
    elif cards == [2, 3]:
        return 5
    elif cards == [1, 1, 3]:
        return 4
    elif cards == [1, 2, 2]:
        return 3
    elif cards == [1, 1, 1, 2]:
        return 2
    elif cards == [1, 1, 1, 1, 1]:
        return 1

def convert_hand(hand, p2):
    val = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    if p2:
        val = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    
    card = []
    for i in range(len(hand)):
        card.append(val.index(hand[i]) + 1)

    return tuple(card)

def part_one():
    hands = []
    sum = 0;

    for l in ll:
        hand, bid = l.split()
        hand = convert_hand(hand, False)
        ranking = get_ranking(hand, False)
        hands.append((ranking, hand, int(bid)))

    hands = sorted(hands, key=lambda x: (x[0], x[1]))

    for idx, h in enumerate(hands):
        sum += h[2] * (idx + 1) 

    print("one", sum)

def part_two():
    hands = []
    sum = 0;

    for l in ll:
        hand, bid = l.split()
        hand = convert_hand(hand, True)
        ranking = get_ranking(hand, True)
        hands.append((ranking, hand, int(bid)))

    hands = sorted(hands, key=lambda x: (x[0], x[1]))

    for idx, h in enumerate(hands):
        sum += h[2] * (idx + 1) 

    print("two", sum)

part_one()
part_two()
