from random import shuffle

# Function dealing a new hand
###########################################
def deal():

  # If we wanna get fancy, we could use the ASCII symbols for clubs, hearts, etc.
  suits = 'C', 'D', 'H', 'S' 
  faces = '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
  # generates a deck with all 32 cards
  deck = [f+s for s in suits for f in faces]
  # shuffles the deck,
  shuffle(deck)
  # "Dealing" hands to the 4 players
  return deck[:8], deck[8:16], deck[16:24], deck[24:]

# Checking hand for consequtive cards
###########################################
def find_consequtives(hand):
    suits = 'C', 'D', 'H', 'S' 
    faces = '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
    # generates an ordered deck
    deck = [f+s for s in suits for f in faces]

    positions = [i for i in range(35)]
    del num[8::9] #This remove positions 8, 17 and 26, separating the list into 4 groups for 4 suits
    # This dict gives an index to each card
    sequence_dict = seq = {k: v for k, v in zip(deck, positions)}

    # Turns card faces to their index from the sequence_dict
    for i in hand:
        cards.append(seq[i])



    current = 1
    ans = 1

    for i in range(len(sorted(cards))-1):
        if sorted(cards)[i] == sorted(cards)[i+1]-1:
            current +=1
        else:
            ans = max(ans, current)
            current = 1
    
    # if max(ans,current) == 3 - terca, if 4 - quarta, if >=5 - quinta 





# calculating team points using a dict and player announcements
###########################################

ann_dict = {
    'belote':20,
    'tierce':20,
    'quarte':50,
    'quinte':100,
    'carre':100,
    'carre_of_9s':150,
    'carre_of_Js':200
}

announcements = ['belote', 'tierce', 'quinte']

points = 0

for a in announcements:
    points += ann_dict[a]

###################################################
class Team():

    def __init__(self, name):
        self.name = name
        self.players = []
        self.points = 0
        self.wins = 0

class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.announcements = []

###################################################

def main():
    pass

if __name__ == '__main__':
        main()    