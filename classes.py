from random import shuffle, choice
from untils import declarations_in, set_t1_lad, set_t2_lad, validate_all

class Player:
    def __init__(self, name, team_name):
        self.name = name
        self.hand = []
        self.all_announcements = []
        self.valid_announcements = []
        self.team_name = team_name
        self.points = 0
        self.team_points = 0
        self.team_wins = 0

    def announce(self):
    	self.all_announcements = declarations_in(self.hand)

class Dealer():
	def __init__(self, list_of_player_instances):
		self.players = list_of_player_instances
		self.round_trump = ''
		self.round_counter = 1
		self.game_counter = 1
		self.team1_lad = 0 #lowest allowed declaration, this = opposing team's highest declaration
		self.team2_lad = 0	#lowest allowed declaration, this = opposing team's highest declaration

	def order(self, round_counter):
	    order = [0, 1, 2, 3]
	    
	    if round_counter <= 4: 
	        round_counter, 
	    else:
	        round_counter = round_counter % 4
	    
	    return order[round_counter-1:]+order[:round_counter-1]

	def dealing(self, order):
		suits = 'C', 'D', 'H', 'S' 
		faces = '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
		deck = [f+s for s in suits for f in faces]
		shuffle(deck)

		self.players[order[0]].hand = deck[:8]
		self.players[order[1]].hand = deck[8:16]
		self.players[order[2]].hand = deck[16:24]
		self.players[order[3]].hand = deck[24:]


	def declare_round_trump(self):
		trumps = ['Clubs', 'Diamonds', 'Hearts', 'Spades', 'No trumps', 'All trumps']
		self.round_trump = choice(trumps)

	def resolve_announcement_conflicts(self, order):
		p = self.players

			p[order][0].announce()
			p[order][0].valid_announcements = validate_all(p[order][0].all_announcements)
			self.team2_lad = set_lad(p[order][0].valid_announcements+p[order][2].valid_announcements)

			p[order][1].announce()
			p[order][1].valid_announcements = validate_all(p[order][1].all_announcements)
			self.team1_lad = set_lad(p[order][1].valid_announcements+p[order][3].valid_announcements)

			p[order][2].announce()
			p[order][2].valid_announcements = validate_all(p[order][2].all_announcements)
			self.team2_lad = set_lad(p[order][0].valid_announcements+p[order][2].valid_announcements)

			p[order][3].announce()
			p[order][3].valid_announcements = validate_all(p[order][3].all_announcements)
			self.team1_lad = set_lad(p[order][1].valid_announcements+p[order][3].valid_announcements)

			p[order][0].valid_announcements = validate_all(p[order][0].all_announcements)
			p[order][1].valid_announcements = validate_all(p[order][1].all_announcements)

	def score_round(): #def add_round_score_to_team_score  
		pass

	def add_round_score_to_results_txt():
		pass

	def add_round_hands_and_announcements_to_data_json():
		pass

	def check_for_wins():
		pass