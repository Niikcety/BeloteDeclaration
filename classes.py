class Player:
    def __init__(self, name, team_name):
        self.name = name
        self.hand = []
        self.announcements = []
        self.team_name = team_name
        self.points = 0
        self.team_points = 0
        self.team_wins = 0

    def announce(self):
    	pass

class Dealer(object):
	def __init__(self, list_of_player_instances):
		self.players = list_of_player_instances
		self.round_counter = 0
		self.game_counter = 0 

	# def order of dealing():
	#	pass
	def dealing():
		pass

	def declare_round_trump():
		pass

	def resolve_announcement_conflicts():
		pass

	def score_round(): #def add_round_score_to_team_score  
		pass

	def add_round_score_to_results_txt():
		pass

	def add_round_hands_and_announcements_to_data_json():
		pass

	def check_for_wins():
		pass
		

