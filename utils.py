suites = ['C', 'D', 'H', 'S']
faces = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [f+s for s in suites for f in faces]

num = [i for i in range(35)]
del num[8::9] 
'''This removes 8, 17 & 26 from the list. 
The idea is to give non-sequential values to Aces and 7s 
of different suites in the dictionary below.''' 

seq_dict = {k: v for k, v in zip(deck, num)}

seq_hierarchy = {
    (0, 1, 2) : ['tierce', 3.0],
    (1, 2, 3) : ['tierce', 3.1],
    (2, 3, 4) : ['tierce', 3.2],
    (3, 4, 5) : ['tierce', 3.3],
    (4, 5, 6) : ['tierce', 3.4],
    (5, 6, 7) : ['tierce', 3.5],
    (0, 1, 2, 3) : ['quarte', 4.0],
    (1, 2, 3, 4) : ['quarte', 4.1],
    (2, 3, 4, 5) : ['quarte', 4.2],
    (3, 4, 5, 6) : ['quarte', 4.3],
    (4, 5, 6, 7) : ['quarte', 4.4],
    (0, 1, 2, 3, 4) : ['quinte', 5.0],
    (1, 2, 3, 4, 5) : ['quinte', 5.1],
    (2, 3, 4, 5, 6) : ['quinte', 5.2],
    (3, 4, 5, 6, 7) : ['quinte', 5.3],
    (9, 10, 11) : ['tierce', 3.0],
    (10, 11, 12) : ['tierce', 3.1], 
    (11, 12, 13) : ['tierce', 3.2],
    (12, 13, 14) : ['tierce', 3.3],
    (13, 14, 15) : ['tierce', 3.4],
    (14, 15, 16) : ['tierce', 3.5],
    (9, 10, 11, 12) : ['quarte', 4.0],
    (10, 11, 12, 13) : ['quarte', 4.1], 
    (11, 12, 13, 14) : ['quarte', 4.2],
    (12, 13, 14, 15) : ['quarte', 4.3],
    (13, 14, 15, 16) : ['quarte', 4.4],
    (9, 10, 11, 12, 13) : ['quinte', 5.0],
    (10, 11, 12, 13, 14) : ['quinte', 5.1], 
    (11, 12, 13, 14, 15) : ['quinte', 5.2],
    (12, 13, 14, 15, 16) : ['quinte', 5.3],
    (18, 19, 20) : ['tierce', 3.0],
    (19, 20, 21) : ['tierce', 3.1],
    (20, 21, 22) : ['tierce', 3.2],
    (21, 22, 23) : ['tierce', 3.3],
    (22, 23, 24) : ['tierce', 3.4],
    (23, 24, 25) : ['tierce', 3.5],
    (18, 19, 20, 21) : ['quarte', 4.0],
    (19, 20, 21, 22) : ['quarte', 4.1],
    (20, 21, 22, 23) : ['quarte', 4.2],
    (21, 22, 23, 24) : ['quarte', 4.3],
    (22, 23, 24, 25) : ['quarte', 4.4],
    (18, 19, 20, 21, 22) : ['quinte', 5.0],
    (19, 20, 21, 22, 23) : ['quinte', 5.1],
    (20, 21, 22, 23, 24) : ['quinte', 5.2],
    (21, 22, 23, 24, 25) : ['quinte', 5.3],
    (27, 28, 29) : ['tierce', 3.0],
    (28, 29, 30) : ['tierce', 3.1], 
    (29, 30, 31) : ['tierce', 3.2],
    (30, 31, 32) : ['tierce', 3.3],
    (31, 32, 33) : ['tierce', 3.4],
    (32, 33, 34) : ['tierce', 3.5],
    (27, 28, 29, 30) : ['quarte', 4.0],
    (28, 29, 30, 31) : ['quarte', 4.1],
    (29, 30, 31, 32) : ['quarte', 4.2],
    (30, 31, 32, 33) : ['quarte', 4.3],
    (31, 32, 33, 34) : ['quarte', 4.4],
    (27, 28, 29, 30, 31) : ['quinte', 5.0],
    (28, 29, 30, 31, 32) : ['quinte', 5.1],
    (29, 30, 31, 32, 33) : ['quinte', 5.2],
    (30, 31, 32, 33, 34) : ['quinte', 5.3]
    }

def validate_all(all_ann, lad):
    control = []

    for ann in all_ann:
        
        if tuple(ann) not in seq_hierarchy:
            control.append(ann)
        elif seq_hierarchy[tuple(ann)][1] >= lad:
            control.append(ann)

    return control


def set_lad(opposing_ann):
    control = []

    for ann in opposing_ann:
        
        if tuple(ann) in seq_hierarchy:
            control.append(seq_hierarchy[tuple(ann)][1])

    try:
        return max(control)
    except:
        return 0


def resolve(sequences, control):
    resolved_s = []

    for seq in sequences:

        if len(seq) == 1:
            pass

        elif len(seq) == 2 and seq == [5, 6] or seq == [14, 15] or seq == [23, 24] or seq == [32, 33]:
            resolved_s.append(seq)
        
        elif len(seq) > 2 and not any(c in seq for con in control for c in con):
            resolved_s.append(seq)

    return resolved_s

def seq_in(cards, control=[]):
    sequences = []

    for i, card in enumerate(cards):

        if i == 0:
            sequences.append([])
            sequences[i].append(card)

        elif i != 0 and sequences[-1][-1] == card-1:
            sequences[-1].append(card)

        else:
            sequences.append([])
            sequences[-1].append(card)

    return resolve(sequences, control)

def carre_in(cards):
    result = []

    for i in cards:

        if i == 0 or i == 1:
            pass

        elif i == 2:
            if i+9 and i+18 and i+27 in cards:
                result.append([2, 11, 20, 29])

        elif i == 3:
            if i+9 and i+18 and i+27 in cards:
                result.append([3, 12, 21, 30])

        elif i == 4:
            if i+9 and i+18 and i+27 in cards:
                result.append([4, 13, 22, 31])

        elif i == 5:
            if i+9 and i+18 and i+27 in cards:
                result.append([5, 14 ,23, 32])

        elif i == 6:
            if i+9 and i+18 and i+27 in cards:
                result.append([6, 15, 24, 33])

        elif i == 7:
            if i+9 and i+18 and i+27 in cards:
                result.append([7, 16, 25, 34])
    return result

def numbify(hand):
    cards = []

    for card in hand:
        cards.append(seq_dict[card])

    return sorted(cards)

def declarations_in(hand):
    cards = numbify(hand)
    carre = carre_in(cards)
    seqs = seq_in(cards, carre)

    return [seqs, carre]

