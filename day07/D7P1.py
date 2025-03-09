import functools
conv = {'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        9: 9,
        8:8,
        7:7,
        6:6,
        5:5,
        4:4,
        3:3,
        2:2,
        '9': 9,
        '8':8,
        '7':7,
        '6':6,
        '5':5,
        '4':4,
        '3':3,
        '2':2}

def comphand(hand1, hand2):
    hand1c = []
    for x in set(hand1[0]):
        hand1c.append([x,hand1[0].count(x)])
    hand1c.sort(key = lambda x: x[1], reverse=True)
    hand2c = []
    for x in set(hand2[0]):
        hand2c.append([x, hand2[0].count(x)])
    hand2c.sort(key=lambda x: x[1],reverse=True)
    hand1s = strength(hand1c)
    hand2s = strength(hand2c)
    if type(hand1s) == int and type(hand2s) == int:
        if hand1s > hand2s:
            return 1
        elif hand2s > hand1s:
            return -1
        else:
            i = 0
            while i < 5:
                if conv[hand1[0][i]] > conv[hand2[0][i]]:
                    return 1
                elif conv[hand1[0][i]] < conv[hand2[0][i]]:
                    return -1
                else:
                    i += 1
    if type(hand1s) == int and type(hand2s) != int:
        return 1
    if type(hand1s) != int and type(hand2s) == int:
        return -1
    if type(hand1s) != int and type(hand2s) != int:
        if conv[hand1s] > conv[hand2s]:
            return 1
        elif conv[hand1s] < conv[hand2s]:
            return -1
        else:
            i = 0
            while i < 5:
                if conv[hand1[0][i]] > conv[hand2[0][i]]:
                    return 1
                elif conv[hand1[0][i]] < conv[hand2[0][i]]:
                    return -1
                else:
                    i += 1


def strength(hand):
    if hand[0][1] == 5:
        return 6
    elif hand[0][1] == 4:
        return 5
    elif len(hand) >1 and hand[0][1] == 3 and hand[1][1] == 2:
        return 4
    elif len(hand) >1 and hand[0][1] == 3 and hand[1][1] == 1:
        return 3
    elif len(hand) >1 and hand[0][1] == 2 and hand[1][1] == 2:
        return 2
    elif len(hand) >1 and hand[0][1] == 2 and hand[1][1] <2:
        return 1
    elif hand[0][1] == 1:
        max = conv[hand[0][0]]
        maxi = hand[0][0]
        for fasz in hand:
            if conv[fasz[0]] > max:
                max = conv[fasz[0]]
                maxi = fasz[0]
        return maxi

lines = []
with open("input (2).txt", "r") as file:
    for line in file:
        line = line.strip().split()
        lines.append([line[0], int(line[1])])
lines = sorted(lines,key=functools.cmp_to_key(comphand))
print(lines)
szum = 0
for i, line in enumerate(lines,1):
    szum += i*line[1]
print(szum)
