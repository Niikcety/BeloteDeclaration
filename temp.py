from random import shuffle, choice

''' Notes from Discord call'''

# class Team:
#   def __init__(self, name, player1, player2):
#       self.name = name
#       self.players = []
#       self.points = 0
#       self.wins = 0



class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.announcements = []
        self.team_name = "Mecheta"
        self.points = 0
        self.team_points = 0
        self.team_wins = 0

    def announce # = check cards for tricks and add them to announcements

class Dealer(p1, p2, p3, p4)
    def __init__(teams):
        self.teams
        self.players = teams[0].players[0]
        self.round_number
        self.game_number

    # def order of dealing 
    def dealing 
    def declare_round_trump 
    def resolve_announcement_conflicts 
    
    def score_round   60 100   #def add_round_score_to_team_score  
    def add_round_score_to_results_txt
    def add_round_hands_and_announcements_to_data_json
    def check_for_wins

''' Notes from Discord call'''

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

player.announcements = ['belote', 'tierce', 'quinte']

team.points = 0

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

# Randomly choose trump for a round
###################################################
def choose_trump():
    trumps = ['clubs', 'diamonds', 'hearts', 'spades', 'no trumps', 'all trumps']
    return choice(trumps)


# Rotate order
###################################################
def order(round_number):
    positions = ['N', 'E', 'S', 'W']
    
    if round_number <= 4: 
        round_number, 
    else: 
        round_number % 4
    
    return positions[round_number:]+positions[:round_number]

def main():
    pass

if __name__ == '__main__':
        main()    