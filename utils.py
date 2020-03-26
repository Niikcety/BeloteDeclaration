suites = ['C', 'D', 'H', 'S']
faces = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [f+s for s in suites for f in faces]

num = [i for i in range(35)]
del num[8::9] 
'''This removes 8, 17 & 26 from the list. 
The idea is to give non-sequential values to Aces and 7s 
of different suites in the dictionary below.''' 

seq_dict = {k: v for k, v in zip(deck, num)}

def seq_in(cards):
	ans = 1
	tmp = 1

	for i in range(len(cards)-1):

	    if sorted(cards)[i]+1 == sorted(cards)[i+1]:
	        tmp +=1
	    else:
	        ans = max(ans, tmp)
	        tmp = 1
	        
def carre_in(cards):
	result = []

	for i in cards:

		if i == 0 or i == 1:
			pass

		elif i == 2:
			if i+9 and i+18 and i+27 in cards:
				result.append('carre_of_9s')

		elif i == 3:
			if i+9 and i+18 and i+27 in cards:
				result.append('carre_of_10s')

		elif i == 4:
			if i+9 and i+18 and i+27 in cards:
				result.append('carre_of_Js')

		elif i == 5:
			if i+9 and i+18 and i+27 in cards:
				result.append('carre_of_Qs')

		elif i == 6:
			if i+9 and i+18 and i+27 in cards:
				result.append('carre_of_Ks')

		elif i == 7:
			if i+9 and i+18 and i+27 in cards:
				result.append('carre_of_As')

	return result

def numbify(hand):
	cards = []

	for card in hand:
		cards.append(seq_dict[card])

	return sorted(cards)

def declarations_in(hand):
	cards = numbify(hand)
	carre_in(cards)
	seq_in(cards)

	