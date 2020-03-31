from dicts import (
    int_of_card_dict, 
    belote_dict,
    carre_dict,
    tqq_dict,
    lad_dict
    )

def validate_tqq(tqq, lad):
    string = []
    points = 0

    for t in tqq:
        if tqq_dict[t][2] > lad:
            string.append(tqq_dict[t][0])
            points += tqq_dict[t][1]

    return string, points

def validate_carres(carres):
    string = []
    points = 0

    for car in carres:
        if car == (0,):
            pass

        else:
            string.append(carre_dict[car][0])
            points += carre_dict[car][1]

    return string, points

def validate_belotes(belotes, trump):
    string = []
    points = 0

    for bel in belotes:
        if bel == (0,):
            pass

        elif bel == (5, 6):
            if trump == 'Clubs' or trump == 'All trumps':
                string.append(belote_dict[bel][0])
                points += belote_dict[bel][1]

        elif bel == (14, 15):
            if trump == 'Diamonds' or trump == 'All trumps':
                string.append(belote_dict[bel][0])
                points += belote_dict[bel][1]

        elif bel == (23, 24):
            if trump == 'Hearts' or trump == 'All trumps':
                string.append(belote_dict[bel][0])
                points += belote_dict[bel][1]

        elif bel == (32, 33):
            if trump == 'Spades' or trump == 'All trumps':
                string.append(belote_dict[bel][0])
                points += belote_dict[bel][1]

    return string, points

def validate_all(announcements, trump, lad=0):
    anns = []
    points = 0

    anns += validate_belotes(announcements[0], trump)[0]
    points += validate_belotes(announcements[0], trump)[1]

    anns += validate_carres(announcements[1])[0]
    points += validate_carres(announcements[1])[1]

    anns += validate_tqq(announcements[2], lad)[0]
    points += validate_tqq(announcements[2], lad)[1]

    return anns, points

def set_lad(opposing_announcements):
    control = []

    for ann in opposing_announcements:
        control.append(lad_dict[ann])

    try:
        return max(control)
    except ValueError:
        return 0

def check_if(sequences, carre):
    checked_tqq = []

    for seq in sequences:

        if len(seq) < 3:
            pass
        
        elif not any(s in seq for c in carre for s in c):
            checked_tqq.append(tuple(seq))

    if checked_tqq == []:
        checked_tqq.append((0,))

    return checked_tqq

def tqq_in(cards, carre=[]):
    tqq = []

    for i, card in enumerate(cards):

        if i == 0:
            tqq.append([])
            tqq[i].append(card)

        elif i != 0 and tqq[-1][-1] == card-1:
            tqq[-1].append(card)

        else:
            tqq.append([])
            tqq[-1].append(card)

    return check_if(tqq, carre)

def carres_in(cards):
    carres = []
    
    for i in range(2,8):
        j = i + 9
        k = i + 18
        l = i + 27

        if i in cards and j in cards and k in cards and l in cards:
            carres.append((i, j, k, l))

    if carres == []:
        carres.append((0,))
    
    return carres

def belotes_in(cards):
    belotes = []

    for i in range(5, 34, 9):
        j = i + 1

        if i in cards and j in cards:
            belotes.append((i, j))

    if belotes == []:
        belotes.append((0,))

    return belotes

def numbify(hand):
    cards = []

    for card in hand:
        cards.append(int_of_card_dict[card])

    return sorted(cards)

def declarations_in(hand):
    cards = numbify(hand)

    belotes = belotes_in(cards)
    carres = carres_in(cards)
    tqq = tqq_in(cards, carres) #tqq = tierce, quarte, quinte

    return [belotes, carres, tqq]