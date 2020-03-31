from dicts import (
    int_of_card_dict, 
    belote_dict,
    carre_dict,
    tqq_dict
    )

def validate_all(all_ann, lad=0):
    control = []

    for ann in all_ann:
        try:
    # if ann not in dict, ann is belote or carre  
            if tuple(ann[0]) not in seq_hierarchy:
                control.append(ann)
            elif seq_hierarchy[tuple(ann[0])][1] >= lad:
                control.append(ann)
        except IndexError:
            pass
    return control


def set_lad(opposing_ann):
    control = []

    for ann in opposing_ann:
        
        if tuple(ann[0]) in seq_hierarchy:
            control.append(seq_hierarchy[tuple(ann[0])][1])

    try:
        return max(control)
    except:
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
    carres = carre_in(cards)
    tqq = tqq_in(cards, carre) #tqq = tierce, quarte, quinte

    return [belotes, carres, tqq]

