suites = ['C', 'D', 'H', 'S']
faces = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [f+s for s in suites for f in faces]

num = [i for i in range(35)]
del num[8::9] 
'''This removes 8, 17 & 26 from the list. 
The idea is to give non-sequential values to Aces and 7s 
of different suites in the dictionary below.''' 

seq_dict = {k: v for k, v in zip(deck, num)}

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
	seq_in(cards, carre)

	